import os
from distutils.core import setup, Command
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
with open("LICENSE.txt", "r", encoding="utf-8") as fh:
    license = fh.read()

setup(
    name = 'yap',
    version = '0.0.1',
    description = 'Yet Another Package-Manager',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author = 'Alessandro Mazzoli',
    author_email = 'developer.alessandro.mazzoli@gmail.com',
    license = license,
    url = 'https://github.com/alemazzo/yap',
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.6',
    scripts=['main.py']
)


