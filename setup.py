import os

from setuptools import find_packages, setup

version_contents = {}
version_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "taceconomics/version.py"
)

with open(version_path, "rt") as f:
    exec(f.read(), version_contents)


setup(
    name="taceconomics",
    description="Python client library for TAC ECONOMICS API",
    version=version_contents["VERSION"],
    install_requires=[
        "requests>=2.20",
        "pandas>=1.2.3",
    ],
    python_requires=">=3.6",
    packages=find_packages(exclude=["tests", "tests.*"]),
    author="TAC ECONOMICS",
    author_email="info@taceconomics.com",
    url="https://github.com/taceconomics/taceconomics-python",
)