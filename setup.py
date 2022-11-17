from os import linesep

from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as read_me:
    LONG_DESCRIPTION = linesep + read_me.read()

setup(
    name="cli-utilities",
    version="0.0.1",
    author="Vishv Patel (itsthevp)",
    description="CLI Utilities",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/itsthevp/cli-utils",
    license="MIT",
    python_requires=">=3.6.0",
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    entry_points={"console_scripts": []},
)