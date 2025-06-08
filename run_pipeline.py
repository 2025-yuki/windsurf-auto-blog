# run_pipeline.py
"""
GitHub Actions から呼び出す WindSurf AUTO SEO Writer のエントリポイント。
 - auto_seo.yaml を読み込み
 - WindSurf の run_pipeline() を起動
 - Slack にテスト通知を送る
"""

from pathlib import Path
import os
import requests
from windsurf.model import run_pipeline  # vendor した openearth/windsurf の関数

def main() -> None:
    # YAML を取得して実行
    yaml_path = Path(__file__).with_name("auto_seo.yaml")
    print(f"🚀 Running pipeline with YAML: {yaml_path}")
    run_pipeline(str(yaml_path))
    print("✅ run_pipeline() 完了")

    # Slack テスト通知
    webhook = os.getenv("SLACK_WEBHOOK_URL")
    if webhook:
        resp = requests.post(
            webhook,
            json={"text": "✅ WindSurf AUTO Writer テスト通知 (from run_pipeline.py)"}
        )
        if resp.status_code == 200:
            print("✅ Slack へ通知成功")
        else:
            print(f"❌ Slack 通知失敗: {resp.status_code} {resp.text}")
    else:
        print("⚠️ SLACK_WEBHOOK_URL が未設定のため Slack 送信スキップ")

if __name__ == "__main__":
    main()