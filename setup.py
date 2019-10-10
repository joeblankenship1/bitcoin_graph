import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="bitcoin_graph",
    version="0.1a1",
    description="A Python library for making matrices and graphs of Bitcoin wallet transactions",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/joeblankenship1/bitcoin_graph",
    author="Joe Blankenship",
    author_email="info@cgrii.org",
    license="GPL-3.0",
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "blockchain==1.4.4",
        "networkx==2.3"
    ],
)
