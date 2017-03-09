# What is this?

This is a template for a Firefox Telemetry ETL job, meant to be used with [cookiecutter](https://cookiecutter.readthedocs.io/).
This tool creates the boilerplate necessary to create a simple ETL job scheduled over [ATMO](https://analysis.telemetry.mozilla.org/)
(including tests!!)

# Testing

Tests are run with [pytest](http://doc.pytest.org/en/latest/getting-started.html#our-first-test-run).
If you get import errors when running the tests, try installing the package in editable mode:

```bash
pip install -e .
```

If you see errors for a py4j KeyError, upgrade py4j with: `pip install py4j --upgrade`

# Appendix

This work is inspired by [cookiecutter-python-cli](https://github.com/nvie/cookiecutter-python-cli)
