# run_pipeline.py
"""
WindSurf AUTO SEO Writer – console.py 直接実行版
"""

from pathlib import Path
import subprocess
import sys


def main() -> None:
    repo_root = Path(__file__).parent
    yaml_path = repo_root / "auto_seo.yaml"
    console_py = repo_root / "vendor" / "windsurf" / "windsurf" / "console.py"

    print(f"🚀 python {console_py} run {yaml_path}")

    subprocess.run(
        [sys.executable, str(console_py), "run", str(yaml_path)],
        check=True,
    )


if __name__ == "__main__":
    main()
