#!/usr/bin/env python3
"""Fetch Stanford ExploreCourses catalogs and normalize them to JSON.

Usage:
    python scripts/fetch_catalog.py

Data source: https://explorecourses.stanford.edu (public XML API).
The raw XML is cached under data/raw/ so the build is reproducible offline.
"""

from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "catalog.json"

SUBJECTS = [
    "CS", "EE", "STATS", "CME", "MS&E", "AA",
    "PSYCH", "LING", "SYMSYS", "ME", "BIOE", "EDUC",
]
ACADEMIC_YEAR = "20262027"
BASE = "https://explorecourses.stanford.edu/search"


def fetch(subject: str) -> str:
    params = {
        "view": "xml-20200810",
        "academicYear": ACADEMIC_YEAR,
        "filter-departmentcode-" + subject: "on",
        "filter-coursestatus-Active": "on",
        "q": subject,
    }
    url = BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "stanford-ai-courses/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read().decode("utf-8", errors="replace")


def text(node: ET.Element | None) -> str:
    if node is None:
        return ""
    return re.sub(r"\s+", " ", "".join(node.itertext())).strip()


def parse(xml: str) -> list[dict]:
    root = ET.fromstring(xml)
    courses = []
    for c in root.findall(".//course"):
        terms, instructors, pis = [], [], []
        for sec in c.findall("./sections/section"):
            term = text(sec.find("term"))
            if term and term not in terms:
                terms.append(term)
            for inst in sec.findall("./schedules/schedule/instructors/instructor"):
                name = text(inst.find("name"))
                if not name:
                    continue
                if name not in instructors:
                    instructors.append(name)
                if text(inst.find("role")) == "PI" and name not in pis:
                    pis.append(name)
        courses.append({
            "subject": text(c.find("subject")),
            "code": text(c.find("code")),
            "title": text(c.find("title")),
            "description": text(c.find("description")),
            "grading": text(c.find("grading")),
            "units_min": text(c.find("unitsMin")),
            "units_max": text(c.find("unitsMax")),
            "terms": terms,
            "instructors": instructors,
            "instructors_pi": pis or instructors,
            "course_id": text(c.find("./administrativeInformation/courseId")),
        })
    return courses


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    all_courses: dict[str, dict] = {}
    for subject in SUBJECTS:
        cache = RAW / f"{subject.replace('&', '_')}.xml"
        if cache.exists() and cache.stat().st_size > 500:
            print(f"using cached {subject} ...", flush=True)
            xml = cache.read_text(encoding="utf-8")
        else:
            print(f"fetching {subject} ...", flush=True)
            xml = fetch(subject)
            cache.write_text(xml, encoding="utf-8")
        parsed = parse(xml)
        print(f"  {len(parsed)} courses")
        for course in parsed:
            key = f"{course['subject']} {course['code']}"
            course["id"] = key
            course["slug"] = re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")
            all_courses.setdefault(key, course)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(sorted(all_courses.values(), key=lambda c: (c["subject"], c["code"])),
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"wrote {len(all_courses)} courses -> {OUT}")


if __name__ == "__main__":
    main()
