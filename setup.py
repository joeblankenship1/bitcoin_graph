import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="bitcoin_graph",
    version="19.0.1",
    description="A Python library for making matrices and graphs of Bitcoin wallet transactions",
    long_description="The bitcoin_graph library makes it simple to produce graphs and matrices of Bitcoin transactions from a single wallet address of a list of wallet addresses.",
    long_description_content_type="text/markdown",
    url="https://github.com/joeblankenship1/bitcoin_graph",
    author="Joe Blankenship",
    author_email="joe@cgrii.org",
    license="GPL-3.0",
    classifiers=[
        "License :: OSI Approved :: GPL-3.0 License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    packages=[
        "bitcoin_graph"
    ],
    include_package_data=True,
    install_requires=[
        "blockchain",
        "networkx"
    ],
)
