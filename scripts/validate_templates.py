#!/usr/bin/env python3
"""MarkdownテンプレートにH1見出しと内容があることを検査する。"""
from __future__ import annotations
import argparse
from pathlib import Path
def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("directory", type=Path); args = parser.parse_args()
    files = sorted(args.directory.glob("*.md")) if args.directory.is_dir() else []
    errors = [] if files else [f"{args.directory}: Markdownテンプレートがありません"]
    for path in files:
        text = path.read_text(encoding="utf-8").strip()
        if not text.startswith("# "): errors.append(f"{path}: H1見出しがありません")
        if len(text.splitlines()) < 4: errors.append(f"{path}: 内容が不足しています")
    if errors: print("\n".join(errors)); return 1
    print(f"OK: {len(files)} template(s) validated"); return 0
if __name__ == "__main__": raise SystemExit(main())
