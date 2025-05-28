# run_pipeline.py
import subprocess
from pathlib import Path

PIPELINE_YML = "auto_seo.yaml"

def main() -> None:
    """
    GitHub Actions から呼び出されるエントリーポイント。
    vendor フォルダに置いた openearth/windsurf を console-script で実行する。
    """
    root = Path(__file__).resolve().parent
    yaml = root / PIPELINE_YML

    # pip が生成した console-script “windsurf” を呼び出す
    subprocess.run(["windsurf", "run", str(yaml)], check=True)

if __name__ == "__main__":
    main()
