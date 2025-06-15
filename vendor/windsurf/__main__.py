"""WindSurf CLI entry point (production)."""

from vendor.windsurf.windsurf.model import WindsurfWrapper

def run_pipeline() -> None:
    """Run full WindSurf pipeline with WordPress posting."""
    # configfile と必要引数は WindsurfWrapper.__init__ に合わせて変更
    WindsurfWrapper(configfile="auto_seo.yaml").start()

if __name__ == "__main__":
    run_pipeline()
