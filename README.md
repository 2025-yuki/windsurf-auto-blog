# WindSurf Auto Blog 🚀

Google Sheet で管理したキーワード／構成をもとに  
**AI が毎日 1 本の SEO 記事を生成 → WordPress に自動投稿**  
までを GitHub Actions + WindSurf で完全自動化するプロジェクトです。

---

## 目次

1. [システム構成](#システム構成)
2. [リポジトリ構成](#リポジトリ構成)
3. [必要な Secrets](#必要な-secrets)
4. [初回セットアップ](#初回セットアップ)
5. [ワークフローの動き](#ワークフローの動き)
6. [手動実行 & スケジュール変更](#手動実行--スケジュール変更)
7. [よくあるエラーと対処](#よくあるエラーと対処)
8. [ライセンス](#ライセンス)

---

## システム構成

```mermaid
graph LR
  A[Google Spreadsheet] -->|記事ネタ/構成| B(WindSurf Pipeline)
  B -->|本文 / 画像| C[WordPress Site]
  B -->|結果ログ| A
  B -->|結果通知| D[Slack]
  E(GitHub Actions) -. トリガー .-> B
