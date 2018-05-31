from __future__ import print_function

import re
import sys

import setuptools

REQUIREMENTS = [
    "kazoo==2.0",
]

# Regex matching pattern  followed by 3 numerical values separated by .
pattern = re.compile("[0-9]+\.[0-9]+\.?[0-9]*")


def get_version():
    with open("CHANGELOG.md", "r") as fn:
        while True:
            version = pattern.findall(fn.readline())
            if len(version) > 0:
                return "".join(version[0])


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "requirements":
        for req in REQUIREMENTS:
            print(req)
        sys.exit(0)

    setuptools.setup(
        name="runners",
        version=get_version(),
        author="EDITD",
        author_email="engineering@editd.com",
        packages=setuptools.find_packages(),
        scripts=[],
        url="https://github.com/EDITD/runners",
        license="LICENSE.txt",
        description="Help with running stuff",
        long_description="View the github page " +
            "(https://github.com/EDITD/runners) for more details.",
        install_requires=REQUIREMENTS,
    )
