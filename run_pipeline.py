# run_pipeline.py
import subprocess
import sys
from pathlib import Path

# -------- 設定 ----------
PIPELINE_YML = "auto_seo.yaml"
# ------------------------

def main() -> None:
    repo_root = Path(__file__).resolve().parent
    yaml_path = repo_root / PIPELINE_YML

    # WindSurf を “python -m” で実行
    subprocess.run(
        [sys.executable, "-m", "windsurf", "run", str(yaml_path)],
        check=True,
    )

if __name__ == "__main__":
    main()
