#!/usr/bin/env python3
"""Verify every Bilibili link in data/lectures/*.json.

Usage:
    python scripts/verify_bilibili.py

Writes data/bilibili_status.json. Exits non-zero when any link is dead so the
scheduled GitHub Actions run fails loudly.
"""

from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LECTURES = ROOT / "data" / "lectures"
OUT = ROOT / "data" / "bilibili_status.json"
API = "https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Referer": "https://www.bilibili.com/",
}


def load_lectures() -> dict:
    merged: dict = {}
    for path in sorted(LECTURES.glob("*.json")):
        merged.update(json.loads(path.read_text(encoding="utf-8")))
    return merged


def check(bvid: str) -> dict:
    url = API.format(bvid=bvid)
    request = urllib.request.Request(url, headers=HEADERS)
    try:
        payload = json.loads(urllib.request.urlopen(request, timeout=25).read().decode("utf-8"))
        if payload.get("code") != 0:
            return {"ok": False, "error": f"code={payload.get('code')} {payload.get('message')}"}
        data = payload["data"]
        return {
            "ok": True,
            "title": data["title"],
            "owner": data["owner"]["name"],
            "duration": data["duration"],
            "views": data["stat"]["view"],
        }
    except Exception as exc:  # noqa: BLE001 - report any network error as a dead link
        return {"ok": False, "error": str(exc)[:120]}


def main() -> int:
    lectures = load_lectures()
    results = []
    for course_id, entry in lectures.items():
        for label, url in entry.get("bilibili", []):
            bvid = url.rstrip("/").split("/")[-1]
            result = {"course": course_id, "label": label, "url": url, "bvid": bvid, **check(bvid)}
            results.append(result)
            state = "ok" if result["ok"] else "DEAD"
            print(f"{course_id:10} {bvid:14} {state}")

    dead = [item for item in results if not item["ok"]]
    payload = {
        "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total": len(results),
        "ok": len(results) - len(dead),
        "dead": len(dead),
        "items": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"checked {len(results)} links: {len(results) - len(dead)} ok, {len(dead)} dead -> {OUT.relative_to(ROOT)}")
    return 1 if dead else 0


if __name__ == "__main__":
    raise SystemExit(main())
