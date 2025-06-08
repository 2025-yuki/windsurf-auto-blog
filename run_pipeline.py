# run_pipeline.py
"""
WindSurf AUTO SEO Writer のエントリポイント（CLI 版）

- vendor/windsurf/bin/windsurf run auto_seo.yaml を呼び出す
- 失敗すれば GitHub Actions も失敗する
"""

from pathlib import Path
import subprocess
import os
import stat

def main() -> None:
    repo_root = Path(__file__).parent          # windsurf-auto-blog/
    yaml_path  = repo_root / "auto_seo.yaml"
    cli_path   = repo_root / "vendor" / "windsurf" / "bin" / "windsurf"

    print(f"🚀 CLI で WindSurf 実行: {yaml_path}")

    # 実行権限が無ければ付与（CI 用）
    cli_path.chmod(cli_path.stat().st_mode | stat.S_IXUSR)

    # WindSurf CLI を実行
    subprocess.run([str(cli_path), "run", str(yaml_path)], check=True)

if __name__ == "__main__":
    main()