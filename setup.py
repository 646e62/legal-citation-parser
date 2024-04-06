from setuptools import setup, find_packages

setup(
    name='legal_citation_parser',
    version='0.1.3',
    description='Extract metadata from legal citation strings',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    # include any other package metadata here
)
