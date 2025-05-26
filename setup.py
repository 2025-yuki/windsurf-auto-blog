from setuptools import setup, find_packages

setup(
    name="windsurf",
    version="0.1.0",
    packages=find_packages(include=["windsurf", "windsurf.*"]),
    entry_points={
        "console_scripts": ["windsurf=windsurf.console:windsurf"]
    },
)
