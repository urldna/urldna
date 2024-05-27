from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'urlDNA python package'
LONG_DESCRIPTION = 'urlDNA is a powerful tool for comprehensive URL analysis, advanced brand monitoring, phishing detection, and custom query capabilities. This Python package allows users to interact with the urlDNA API seamlessly through Python.'

setup(
    name="urlDNA", 
    version=VERSION,
    author="urlDNA",
    license="MIT License",
    url="https://urldna.io",
    author_email="urldna@urldna.io",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["requests", "marshmallow"],
    keywords=['python', 'web scraping', 'website analysis', 'url scan'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)