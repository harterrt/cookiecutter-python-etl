# What is this?

This is a template for a Firefox Telemetry ETL job.
This repo contains the all of the necessary boilerplate to create a simple ETL job.

## Benefits

To this point, most python ETL jobs were stored in a Jupyter notebook so they could be scheduled in [ATMO](https://analysis.telemetry.mozilla.org/).
By following the best practices in this repo, we fix three major problems:

First, code in a Jupyter notebook is near impossible to test.
We fix this by pulling most of the code out of the Jupyter notebook and into a standard python library.
We also provide example tests to get you started quickly.

Secondly, Jupyter notebooks do not behave well with version control.
The notebook is stored in JSON, with terminal output,
so diffs are noisy and it's difficult for the reviewer to digest the commit.
Combine this with the lack of tests and you can see how difficult reviewing an analysis can be.

Finally, while scheduling a job in ATMO is quick and effective, it has some drawbacks.
Updating the job requires the user to manually upload a new Jupyter notebook.
This means we cannot audit which version of an ETL job was running at a certain time in the past.
More so, this leads to a pile of analyses with names like: testpilot_analysis(3)_fixed_no_nulls.ipynb.

# Testing

Tests are run with [pytest](http://doc.pytest.org/en/latest/getting-started.html#our-first-test-run).
If you get import errors when running the tests, try installing the package in editable mode:

```bash
pip install -e .
```

If you see errors for a py4j KeyError, upgrade py4j with: `pip install py4j --upgrade`

# Scheduling

To schedule your job in ATMO, take a look at [this notebook](scheduling/load_and_run.ipynb).
This notebook downloads and installs your library before running an `etl_job` function.

To schedule your job in [Airflow](https://github.com/mozilla/telemetry-airflow),
take a look at [this example script](scheduling/airflow.sh).
This script will download, install, and run your ETL job.
Check this script into the [`jobs` subfolder](https://github.com/mozilla/telemetry-airflow/tree/master/jobs)
and schedule a new DAG.


# Appendix

This work is inspired by [cookiecutter-python-cli](https://github.com/nvie/cookiecutter-python-cli)
