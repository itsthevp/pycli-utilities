from os import linesep

from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as read_me:
    LONG_DESCRIPTION = linesep + read_me.read()

setup(
    name="pycli-utilities",
    version="0.0.1",
    author="Vishv Patel (itsthevp)",
    description="pyCLI Utilities",
    keywords=["cli", "utils", "cli-utils", "csv", "json"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/itsthevp/pycli-utilities",
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
    entry_points={
        "console_scripts": [
            "csv-validate = source.utilities.csv_validate:run",
            "csv-remove-nulls = source.utilities.csv_remove_nulls:run",
            "csv-remove-column = source.utilities.csv_remove_column:run",
            "csv-shift-column = source.utilities.csv_shift_column:run",
            "csv-split = source.utilities.csv_split:run",
        ]
    },
)
