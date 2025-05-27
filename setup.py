from setuptools import setup, find_packages

setup(
    name="windsurf",
    version="0.1.0",
    # vendor 化した windsurf/ フォルダの中身をパッケージとして検索
    packages=find_packages(where="windsurf", include=["windsurf", "windsurf.*"]),
    # パッケージは windsurf/ の中にあることを指定
    package_dir={"": "windsurf"},
    entry_points={
        "console_scripts": [
            "windsurf=windsurf.console:windsurf"
        ]
    },
)
