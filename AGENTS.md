# AGENTS.md

このリポジトリは、公開可能なセキュリティ運用テンプレート集です。すべて架空のサンプルとして扱い、実在する組織、資産、脆弱性、インシデント、認証情報を含めません。

## 方針

- Python は 3.12 を前提にする
- スクリプトは標準ライブラリ中心で実装する
- テストは pytest で実行する
- 文書は日本語で、事実・推測・判断を区別して記録する

## 禁止事項

- 実在する組織名、個人名、メールアドレス、IPアドレス、ドメイン、社内パスを含めない
- 認証情報、攻撃手順、悪用可能な詳細、未公開の脆弱性情報を含めない
- テンプレートを組織の法令、契約、規程の代替として扱わない

## 検証

```sh
python -m pytest
python scripts/validate_templates.py templates
python scripts/generate_security_checklist.py incident-response
```
