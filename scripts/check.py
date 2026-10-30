import json, re
from pathlib import Path

root = Path(".")
courses = json.loads((root / "data/courses.json").read_text(encoding="utf-8"))
catalog = {c["id"]: c for c in json.loads((root / "data/catalog.json").read_text(encoding="utf-8"))}
src = []
for p in sorted((root / "data/courses").glob("*.json")):
    src.extend(json.loads(p.read_text(encoding="utf-8")))

errors = []
for c in src:
    if c["id"] == "" or c["id"] not in catalog:
        errors.append(f"missing catalog: {c['id']}")
    if c["id"] in c.get("related", []):
        errors.append(f"self-related: {c['id']}")
    doc = root / "courses" / f"{c['slug']}.md"
    if not doc.exists():
        errors.append(f"missing doc: {doc}")
        continue
    text = doc.read_text(encoding="utf-8")
    for section in ["## 课程定位", "## 主要内容", "## 考核与工作量", "## 适合谁", "## 学习建议", "## 相关课程", "## 资源"]:
        if section not in text:
            errors.append(f"{c['id']} missing {section}")
    for m in re.finditer(r"\]\((?!https?://)([^)]+\.md)\)", text):
        target = (doc.parent / m.group(1)).resolve()
        if not target.exists():
            errors.append(f"{c['id']} broken link: {m.group(1)}")

# README links
readme = (root / "README.md").read_text(encoding="utf-8")
for m in re.finditer(r"\]\((?!https?://|#)([^)]+)\)", readme):
    target = (root / m.group(1)).resolve()
    if not target.exists():
        errors.append(f"README broken link: {m.group(1)}")

print(f"courses: {len(src)}, docs: {len(list((root / 'courses').glob('*.md')))}")
print(f"errors: {len(errors)}")
for e in errors:
    print(" -", e)
