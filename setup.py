import setuptools
from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r', encoding='utf-8') as file:
        requirements = []
        for line in file:
            line = line.strip()

            if not line:
                continue

            # if line.startswith("#"):
            #     continue

            if line == HYPHEN_E_DOT:
                continue

            requirements.append(line)

    return requirements


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"
AUTHOR_USER_NAME = "Chandan Pradhan"
AUTHOR_EMAIL = "chandan.pradhan1110@gmail.com"
SRC_REPO = "End-to-End-Deep-Learning----Chicken-Disease-Project"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chandanpradhan1110/End-to-End-Deep-Learning----Chicken-Disease-Project",
    project_urls={
        "Bug Tracker": "https://github.com/chandanpradhan1110/End-to-End-Deep-Learning----Chicken-Disease-Project/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("requirements.txt"),
)
