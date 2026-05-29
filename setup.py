import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "17_TextSummarizer_NLP"
AUTHOR_USER_NAME = "grv08singh"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "grv08singh@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for text summarization using NLP",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)