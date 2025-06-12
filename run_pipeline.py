# run_pipeline.py
"""
GitHub Actions から呼び出す WindSurf AUTO SEO Writer のエントリポイント
------------------------------------------------------------------
1. auto_seo.yaml を読み込み WindSurf pipeline を実行
2. Slack にテスト通知
"""

# ---------- Python2 依存ライブラリを Python3 でだます ----------
import sys, pickle, stat, subprocess, os, requests
sys.modules.setdefault("cPickle", pickle)   # vendor が import cPickle を呼んでも OK
# ---------------------------------------------------------------

from pathlib import Path
from typing import NoReturn

# ------------------------------------------------------------------
# メイン処理
# ------------------------------------------------------------------
def main() -> NoReturn:
    repo_root = Path(__file__).parent       # windsuf-auto-blog/
    yaml_path = repo_root / "auto_seo.yaml"     # パイプライン定義
    cli_path  = repo_root / "vendor" / "windsurf" / "windsurf" / "console.py"

    # ① パイプライン実行
    print("🐍 running WindSurf pipeline...")
    cmd = [
        sys.executable,            # いま実行中の Python (=3.11)
        str(cli_path),
        "run",
        str(yaml_path),
    ]
    print("🚀", *cmd)              # デバッグ出力
    subprocess.run(cmd, check=True)

    # ② Slack へテスト通知
    webhook = os.getenv("SLACK_WEBHOOK_URL")
    if webhook:
        resp = requests.post(webhook, json={
            "text": "✅ WindSurf AUTO Writer テスト通知 (from run_pipeline.py)"
        })
        if resp.status_code == 200:
            print("✅ Slack へ通知成功")
        else:
            print(f"❌ Slack 通知失敗: {resp.status_code} {resp.text}")
    else:
        print("⚠️ SLACK_WEBHOOK_URL が未設定のため Slack 送信スキップ")

    # 正常終了
    print("🎉 run_pipeline.py 完了")

# ------------------------------------------------------------------
if __name__ == "__main__":
    main()