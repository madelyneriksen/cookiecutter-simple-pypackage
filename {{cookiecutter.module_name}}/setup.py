"""
Setup file for {{ cookiecutter.module_name }}
"""


import os
from setuptools import setup


def read(filename):
    """Read a filename as a string"""
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name="{{ cookiecutter.module_name }}",
    version="{{ cookiecutter.version }}",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.description }}",
    url="{{ cookiecutter.project_home }}",
    packages=[],
    long_description=read('README.md'),
)
