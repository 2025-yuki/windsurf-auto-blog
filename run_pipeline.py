# run_pipeline.py
"""
WindSurf AUTO SEO Writer エントリポイント
- vendor/windsurf/windsurf/model.py の run_pipeline() を直接呼び出す
- 実行後 Slack テスト通知
"""

from pathlib import Path
import os
import sys
import requests

# --- vendor/windsurf を import path に追加 ------------------
VENDOR_ROOT = Path(__file__).parent / "vendor" / "windsurf" / "windsurf"
sys.path.insert(0, str(VENDOR_ROOT))

from model import run_pipeline  # type: ignore

def main() -> None:
    yaml_path = Path(__file__).with_name("auto_seo.yaml")
    print(f"🚀 run_pipeline() with {yaml_path}")
    run_pipeline(str(yaml_path))
    print("✅ WindSurf pipeline finished")

    # Slack テスト通知
    webhook = os.getenv("SLACK_WEBHOOK_URL")
    if webhook:
        resp = requests.post(webhook, json={"text": "✅ WindSurf pipeline finished"})
        print("Slack:", resp.status_code, resp.text[:200])

if __name__ == "__main__":
    main()