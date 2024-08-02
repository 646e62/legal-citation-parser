"""
PyPI setup file for legal_citation_parser
"""

from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='legal_citation_parser',
    version='0.4.2',
    description='Extracts metadata from CanLII case citations',
    author='Daniel Nathan Booy',
    url='https://github.com/646e62/legal_citation_parser',
    author_email='444e42@protonmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)
