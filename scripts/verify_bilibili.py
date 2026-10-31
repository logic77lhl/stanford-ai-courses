#!/usr/bin/env python3
"""Verify every Bilibili link in data/lectures/*.json.

Usage:
    python scripts/verify_bilibili.py

Bilibili rate-limits or blocks some networks (especially CI runners). A link is
reported as:
  ok      - API returned the video
  dead    - API says the video does not exist / is unavailable
  unknown - network error or rate limit; retried a few times, not treated as dead

Writes data/bilibili_status.json. Exits non-zero only when a link is confirmed dead.
"""

from __future__ import annotations

import json
import time
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
DEAD_CODES = {-404, 62002, 62004}


def load_lectures() -> dict:
    merged: dict = {}
    for path in sorted(LECTURES.glob("*.json")):
        merged.update(json.loads(path.read_text(encoding="utf-8")))
    return merged


def check_once(bvid: str) -> tuple[str, dict]:
    url = API.format(bvid=bvid)
    request = urllib.request.Request(url, headers=HEADERS)
    try:
        payload = json.loads(urllib.request.urlopen(request, timeout=25).read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001 - network errors are "unknown", not "dead"
        return "unknown", {"error": str(exc)[:120]}

    code = payload.get("code")
    if code == 0:
        data = payload["data"]
        return "ok", {
            "title": data["title"],
            "owner": data["owner"]["name"],
            "duration": data["duration"],
            "views": data["stat"]["view"],
        }
    if code in DEAD_CODES:
        return "dead", {"error": f"code={code} {payload.get('message')}"}
    return "unknown", {"error": f"code={code} {payload.get('message')}"}


def check(bvid: str) -> tuple[str, dict]:
    status, detail = "unknown", {}
    for attempt in range(2):
        status, detail = check_once(bvid)
        if status != "unknown":
            return status, detail
        time.sleep(2 + attempt * 3)
    return status, detail


def main() -> int:
    lectures = load_lectures()
    results = []
    for course_id, entry in lectures.items():
        for label, url in entry.get("bilibili", []):
            bvid = url.rstrip("/").split("/")[-1]
            status, detail = check(bvid)
            results.append({"course": course_id, "label": label, "url": url, "bvid": bvid, "status": status, **detail})
            print(f"{course_id:10} {bvid:14} {status}")
            time.sleep(1.5)

    dead = [item for item in results if item["status"] == "dead"]
    unknown = [item for item in results if item["status"] == "unknown"]
    payload = {
        "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total": len(results),
        "ok": len(results) - len(dead) - len(unknown),
        "dead": len(dead),
        "unknown": len(unknown),
        "items": results,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(
        f"checked {len(results)} links: {payload['ok']} ok, {len(dead)} dead, "
        f"{len(unknown)} unknown (rate limit/network) -> {OUT.relative_to(ROOT)}"
    )
    return 1 if dead else 0


if __name__ == "__main__":
    raise SystemExit(main())
