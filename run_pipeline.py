#!/usr/bin/env python3
"""
WindSurf Auto Blog – minimal pipeline

1.  Google スプレッドシートからキーワードを取得
2.  取得したキーワードで記事本文を生成（現状はダミー）
3.  WordPress に下書きを投稿
4.  Slack に結果を通知

※ 認証情報・詳細処理は省略しているので、環境変数と
   TODO コメントを埋めればそのまま動きます。
"""

import os
import json
import random
import datetime as dt
from pathlib import Path

import openai
import requests
import pandas as pd
from dotenv import load_dotenv

# ------------------------------------------------------------------
# 1. 認証情報の読み込み
# ------------------------------------------------------------------
load_dotenv()  # .env から環境変数を読む

OPENAI_API_KEY      = os.getenv("OPENAI_API_KEY")
GOOGLE_SHEET_ID     = os.getenv("SPREADSHEET_ID")
WP_URL              = os.getenv("WP_URL")
WP_USER             = os.getenv("WP_USER")
WP_APP_PASS         = os.getenv("WP_APP_PASS")
SLACK_WEBHOOK_URL   = os.getenv("SLACK_WEBHOOK_URL")

openai.api_key = OPENAI_API_KEY

# ------------------------------------------------------------------
# 2. キーワード取得（CSV ダミー or Google Sheets）
# ------------------------------------------------------------------
def fetch_keywords() -> list[str]:
    """
    スプレッドシートからキーワード列を取得して list で返す。
    ここでは demo.csv を読むダミー実装。
    """
    csv_path = Path(__file__).with_name("demo.csv")
    if not csv_path.exists():
        raise FileNotFoundError("demo.csv が見つかりません")

    df = pd.read_csv(csv_path)

    # --- ★ 重要: Series → list に変換して random.choice の KeyError を防ぐ ★ --- #
    keywords: list[str] = df["keyword"].dropna().tolist()

    if not keywords:
        raise ValueError("キーワードが 1 件も取得できませんでした")

    return keywords

# ------------------------------------------------------------------
# 3. 記事生成（GPT）
# ------------------------------------------------------------------
def generate_article(keyword: str) -> dict[str, str]:
    """
    OpenAI GPT で記事タイトル・本文を生成
    """
    prompt = f"Write a 300-word Japanese blog post about {keyword}."
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    content = response.choices[0].message.content.strip()

    title = f"{keyword} とは？初心者向け徹底解説（{dt.date.today()}）"
    return {"title": title, "content": content}

# ------------------------------------------------------------------
# 4. WordPress に投稿
# ------------------------------------------------------------------
def post_to_wordpress(post: dict[str, str]) -> int:
    """
    WordPress REST API で下書きを作成し投稿 ID を返す
    """
    url = f"{WP_URL.rstrip('/')}/wp-json/wp/v2/posts"
    auth = (WP_USER, WP_APP_PASS)
    data = {
        "title":   post["title"],
        "content": post["content"],
        "status":  "draft",
    }
    resp = requests.post(url, auth=auth, json=data, timeout=30)
    resp.raise_for_status()
    return resp.json()["id"]

# ------------------------------------------------------------------
# 5. Slack 通知
# ------------------------------------------------------------------
def notify_slack(msg: str) -> None:
    """
    Slack Incoming Webhook にメッセージを送信
    """
    if not SLACK_WEBHOOK_URL:
        print("[WARN] SLACK_WEBHOOK_URL が設定されていないため通知をスキップ")
        return
    requests.post(SLACK_WEBHOOK_URL, json={"text": msg}, timeout=10)

# ------------------------------------------------------------------
# 6. メイン処理
# ------------------------------------------------------------------
def main() -> None:
    keywords = fetch_keywords()
    keyword  = random.choice(keywords)

    post = generate_article(keyword)
    post_id = post_to_wordpress(post)

    notify_slack(f"✅ WindSurf Auto Blog\n新規下書きを作成しました (ID: {post_id})\nタイトル: {post['title']}")

    print(f"[DONE] draft post id = {post_id}")

# ------------------------------------------------------------------
if __name__ == "__main__":
    main()
