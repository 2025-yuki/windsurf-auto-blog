# run_pipeline.py
"""
GitHub Actions から呼び出すエントリポイント。
vendor した openearth/windsurf のモデルを直接実行する。
"""

from pathlib import Path
from windsurf.model import run_pipeline  # ここは openearth 版でも存在する

def main() -> None:
    yaml_path = Path(__file__).with_name("auto_seo.yaml")
    # Google Sheets → WordPress 投稿まで一括実行
    run_pipeline(str(yaml_path))

if __name__ == "__main__":
    main()
