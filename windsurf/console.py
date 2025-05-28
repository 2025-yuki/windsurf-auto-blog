# mock CLI entry-point
import sys
from pathlib import Path
from .model import run_pipeline

def main():
    if len(sys.argv) == 3 and sys.argv[1] == "run":
        run_pipeline(Path(sys.argv[2]))
    else:
        print("usage: windsurf run <yaml>")

if __name__ == "__main__":
    main()
