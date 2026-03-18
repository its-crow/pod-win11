from setuptools import setup

setup(
    name="podgasm",
    version="0.3",
    packages=["podcast"],
    install_requires=[
        "yt-dlp",
    ],
    entry_points={
        "console_scripts": [
            "podcast=podcast:main",
        ],
    },
    include_package_data=True,
)