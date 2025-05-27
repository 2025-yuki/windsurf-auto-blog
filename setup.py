from setuptools import setup, find_packages

setup(
    name="windsurf",
    version="0.1.0",
    # リポジトリ直下にあるすべてのパッケージ(windsurf/)を探す
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "windsurf=windsurf.console:windsurf"
        ]
    },
)
