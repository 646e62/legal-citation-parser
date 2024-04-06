from setuptools import setup, find_packages

# read the contents of your README file one level up
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='legal_citation_parser',
    version='0.1.4',
    description='Extract metadata from legal citations. Currently supports neutral, SCR, and CanLII citations.',
    author='Daniel Nathan Booy',
    url='https://github.com/646e62/legal_citation_parser',
    author_email='444e42@protonmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    # include any other package metadata here
)
