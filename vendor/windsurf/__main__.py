"""
vendor.windsurf を `python -m vendor.windsurf` で実行したときの
エントリポイント。

GitHub Actions から WindSurf の自動 SEO パイプラインを起動する。
"""

# 相対 import で OK。パスが異なる場合は適宜書き換えてください。
from .windsurf.run_pipeline import run_pipeline


def main() -> None:
    """Run the WindSurf pipeline."""
    run_pipeline()


if __name__ == "__main__":
    main()