#!/bin/bash

# We use jupyter by default, but here we want to use python
unset PYSPARK_DRIVER_PYTHON

# Clone, install, and run
git clone https://github.com/harterrt/cookiecutter-python-etl.git
cd cookiecutter-python-etl
pip install .
spark-submit scheduling/airflow_example.py
