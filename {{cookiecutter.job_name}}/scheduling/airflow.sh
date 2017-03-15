#!/bin/bash

# We use jupyter by default, but here we want to use python
unset PYSPARK_DRIVER_PYTHON

# Clone, install, and run
git clone {{cookiecutter.https_github_repo_url}} {{cookiecutter.job_name}}
cd {{cookiecutter.job_name}}
pip install .
spark-submit scheduling/airflow.py
