#!/usr/bin/env python3
"""
Minimal auto-blog pipeline

1.  Google Sheets からキーワードを 1 行ぶん取得
2.  OpenAI で本文を生成
3.  WordPress (XML-RPC) へ下書き投稿
4.  Slack Webhook へ完了通知

環境変数は .env または GitHub Secrets で設定
"""

import os, json, random
from datetime import date

from dotenv import load_dotenv
import openai
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
import requests

# ──────────────────── 0. 設定読み込み
load_dotenv()

GOOGLE_SHEET_JSON = "auto_seo.json"          # キーワード保存用 (ローカル json で代用)
OPENAI_API_KEY    = os.environ["OPENAI_API_KEY"]
WP_URL            = os.environ["WP_URL"]     # 例: https://example.com/xmlrpc.php
WP_USER           = os.environ["WP_USER"]
WP_APP_PASS       = os.environ["WP_APP_PASS"]
SLACK_URL         = os.environ["SLACK_WEBHOOK_URL"]

openai.api_key = OPENAI_API_KEY

# ──────────────────── 1. キーワード取得（今回は json ファイルからランダムに）
with open(GOOGLE_SHEET_JSON, "r", encoding="utf-8") as f:
    keywords: list[str] = json.load(f)

if not keywords:
    raise SystemExit("🙅‍♂️  キーワードがありません")

keyword = random.choice(keywords)
print(f"📝  generate article for: {keyword}")

# ──────────────────── 2. 本文生成
prompt = f"""Write a 600-word Japanese blog post about "{keyword}".
Include an introduction, three headings with paragraphs, and a short conclusion."""
response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
)
article_text: str = response.choices[0].message.content.strip()

title = f"{keyword} – {date.today()}"
print(f"✅  article generated → {len(article_text)} chars")

# ──────────────────── 3. WordPress 投稿（下書き）
wp = Client(WP_URL, WP_USER, WP_APP_PASS)
post          = WordPressPost()
post.title    = title
post.content  = article_text
post.post_status = "draft"

post_id = wp.call(NewPost(post))
print(f"🚀  post created as draft → id={post_id}")

# ──────────────────── 4. Slack 通知
slack_msg = {
    "text": f"✅ 新規下書きを作成しました *{title}* (<{WP_URL.replace('xmlrpc.php','?p='+str(post_id))}|確認>)"
}
requests.post(SLACK_URL, json=slack_msg)
print("📨  notified Slack")
