import os

# Slack に通知を送る簡単なテスト
def send_slack_test_message():
    import requests
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("❌ SLACK_WEBHOOK_URL が設定されていません")
        return
    payload = {
        "text": "✅ WindSurf AUTO Writer テスト通知 (from run_pipeline.py)"
    }
    resp = requests.post(webhook_url, json=payload)
    if resp.status_code == 200:
        print("✅ Slack へ通知成功")
    else:
        print(f"❌ Slack への通知失敗: {resp.status_code}, {resp.text}")

# ここからテスト実行
if __name__ == "__main__":
    main()
    send_slack_test_message()