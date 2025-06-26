from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

VERSION = '0.0.14' 
DESCRIPTION = 'The DNA test for websites.'

setup(
    name="urlDNA", 
    version=VERSION,
    author="urlDNA",
    license="MIT",
    url="https://urldna.io",
    author_email="urldna@urldna.io",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=required,
    keywords=['web scraping', 'website analysis', 'url scan'],
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)