# run_pipeline.py
"""
WindSurf AUTO SEO Writer – openearth/windsurf CLI 実行版
"""

from pathlib import Path
import subprocess
import sys

def main() -> None:
    repo_root = Path(__file__).parent
    yaml_path = repo_root / "auto_seo.yaml"
    winds_cli = repo_root / "vendor" / "windsurf" / "cli.py"

    print(f"🚀 python -m vendor.windsurf.cli run {yaml_path}")

    subprocess.run(
        [sys.executable, str(winds_cli), "run", str(yaml_path)],
        check=True,
    )

if __name__ == "__main__":
    main()
