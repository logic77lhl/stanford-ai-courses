#!/usr/bin/env python3
"""Push the current working tree to GitHub using the REST API.

Useful when git-over-HTTPS is blocked but api.github.com is reachable.
Requires an authenticated `gh` CLI (uses `gh auth token`).

Usage:
    python scripts/push_via_api.py <owner/repo> [branch] [message]
"""

from __future__ import annotations

import base64
import json
import subprocess
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://api.github.com"
EXCLUDE_DIRS = {".git", "data/raw", "__pycache__", ".venv", "venv"}


def token() -> str:
    out = subprocess.check_output(["gh", "auth", "token"], text=True).strip()
    if not out:
        raise SystemExit("gh auth token is empty; run `gh auth login` first")
    return out


def api(method: str, path: str, body: dict | None = None) -> dict:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        API + path,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
            "User-Agent": "stanford-ai-courses-push",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode())


def iter_files():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if any(rel == d or rel.startswith(d + "/") for d in EXCLUDE_DIRS):
            continue
        if rel.endswith((".pyc", ".pyo")):
            continue
        yield path, rel


def make_blob(item):
    path, rel = item
    content = base64.b64encode(path.read_bytes()).decode()
    result = api("POST", f"/repos/{REPO}/git/blobs", {"content": content, "encoding": "base64"})
    return {"path": rel, "mode": "100644", "type": "blob", "sha": result["sha"]}


if __name__ == "__main__":
    REPO = sys.argv[1] if len(sys.argv) > 1 else "logic77lhl/stanford-ai-courses"
    BRANCH = sys.argv[2] if len(sys.argv) > 2 else "main"
    MESSAGE = sys.argv[3] if len(sys.argv) > 3 else "Add Stanford AI/ML/Agent course map"
    TOKEN = token()

    files = list(iter_files())
    print(f"uploading {len(files)} files to {REPO} ...")
    with ThreadPoolExecutor(max_workers=8) as pool:
        entries = list(pool.map(make_blob, files))

    tree = api("POST", f"/repos/{REPO}/git/trees", {"tree": entries})
    print(f"tree: {tree['sha']}")

    # Reuse the existing branch tip as parent when present.
    parents = []
    try:
        ref = api("GET", f"/repos/{REPO}/git/ref/heads/{BRANCH}")
        parents = [ref["object"]["sha"]]
        print(f"parent: {parents[0]}")
    except Exception:
        print("no existing branch; creating an initial commit")

    commit = api("POST", f"/repos/{REPO}/git/commits", {
        "message": MESSAGE,
        "tree": tree["sha"],
        "parents": parents,
    })
    print(f"commit: {commit['sha']}")

    if parents:
        api("PATCH", f"/repos/{REPO}/git/refs/heads/{BRANCH}", {"sha": commit["sha"], "force": True})
    else:
        api("POST", f"/repos/{REPO}/git/refs", {"ref": f"refs/heads/{BRANCH}", "sha": commit["sha"]})

    print(f"pushed: https://github.com/{REPO}/tree/{BRANCH}")
