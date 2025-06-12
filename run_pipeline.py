# run_pipeline.py
"""
WindSurf AUTO SEO Writer – モジュール実行版
"""

from pathlib import Path
import subprocess
import sys


def main() -> None:
    repo_root = Path(__file__).parent
    yaml_path = repo_root / "auto_seo.yaml"

    print(f"🚀 python -m vendor.windsurf run {yaml_path}")

    subprocess.run(
        [sys.executable, "-m", "vendor.windsurf", "run", str(yaml_path)],
        check=True,
    )


if __name__ == "__main__":
    main()
