"""WindSurf CLI entry point (production)."""

from vendor.windsurf.windsurf.model import WindsurfWrapper

def run_pipeline() -> None:
    """Run full WindSurf pipeline with WordPress posting."""
    # ← configfile を JSON に変更
    WindsurfWrapper(configfile="auto_seo.json").start()

if __name__ == "__main__":
    run_pipeline()
