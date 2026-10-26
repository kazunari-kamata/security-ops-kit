# security-ops-kit

脆弱性管理、セキュリティ診断、インシデント対応、再発防止をPDCAで運用するためのテンプレート集です。リスクに基づく判断、証跡、承認、継続的改善の初期ドラフトを提供します。

収録内容はすべて架空のサンプルです。実在する組織、個人、資産、脆弱性、インシデント、認証情報は含めません。

## 内容

- `templates/`: 脆弱性台帳、診断計画、トリアージ、例外承認、インシデント、再発防止、SLA/SLOのテンプレート
- `docs/`: PDCA、インシデント対応、SLA/SLOの運用ガイド
- `scripts/`: テンプレート検証と工程別チェックリスト
- `examples/`: 架空の管理台帳サンプル
- `.github/`: CIとPRテンプレート

## テンプレート一覧

| 領域 | 主なテンプレート |
| --- | --- |
| Plan | セキュリティ運用計画、資産・リスク確認、診断計画 |
| Do | 診断実施記録、脆弱性トリアージ、例外承認 |
| Check | 脆弱性管理台帳、対応状況・指標報告、インシデント記録 |
| Act | 根本原因分析、再発防止計画、振り返り |
| サービス水準 | SLA/SLO定義、測定・報告、例外・改善管理 |
| 基盤管理 | 資産台帳、特権アクセスレビュー、演習、委託先評価 |

## 使い方

1. `docs/security-pdca.md` で工程と判断ポイントを確認します。
2. 対象範囲・権限・緊急連絡・情報分類を組織の規程に合わせて定義します。
3. 脆弱性は影響・悪用可能性・資産重要度・公開状況を根拠とともに評価します。
4. インシデントでは封じ込め、証跡保全、連絡、復旧、再発防止を時系列で記録します。

```sh
python scripts/generate_security_checklist.py vulnerability-triage
python scripts/generate_security_checklist.py incident-response
python scripts/generate_security_checklist.py prevention
python scripts/validate_templates.py templates
python -m pytest
```

## 注意

- 診断・調査は、明示的に許可された対象・時間・手法の範囲で実施してください。
- 実際の脆弱性やインシデント情報は、組織の情報分類・通報・証跡保全のルールに従って管理してください。
- 緊急時の法務・広報・顧客連絡は、権限を持つ担当者の判断と組織の手順に従ってください。
