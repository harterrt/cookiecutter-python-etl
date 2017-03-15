#!/usr/bin/env python

from setuptools import setup, find_packages
from distutils.core import setup

setup(name='{{cookiecutter.job_name}}',
      version='0.1',
      description='{{cookiecutter.job_description}}',
      author='{{cookiecutter.author_name}}',
      author_email='{{cookiecutter.author_email}}',
      url='{{cookiecutter.https_github_repo_url}}',
      packages=find_packages(exclude=['tests']),
)
