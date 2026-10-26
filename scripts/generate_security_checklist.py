#!/usr/bin/env python3
"""セキュリティ運用工程ごとの確認項目を出力する。"""
from __future__ import annotations
import argparse

CHECKLISTS = {
    "vulnerability-triage": ["対象と確認済みの事実を記録した", "影響、到達可能性、資産重要度を評価した", "優先度、担当、期限、判断者を記録した"],
    "incident-response": ["事実・操作・時刻・証跡を時系列で記録した", "封じ込め、連絡、復旧の判断者を確認した", "推測と確認済みの事実を区別した"],
    "prevention": ["根本原因と影響をレビューした", "是正・予防・検知改善の担当と期限を決めた", "効果確認日と残存リスクを記録した"],
    "sla-slo-review": ["SLA/SLOの対象、起点・終点、除外条件を確認した", "目標、実績、傾向、例外を根拠とともに記録した", "未達時の改善策、担当、期限、効果確認日を決めた"],
}
def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("phase", choices=CHECKLISTS); args = parser.parse_args()
    print(f"# {args.phase} checklist")
    for item in CHECKLISTS[args.phase]: print(f"- [ ] {item}")
    return 0
if __name__ == "__main__": raise SystemExit(main())
