from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from {{cookiecutter.job_name}} import main

if __name__ == "__main__":
    conf = SparkConf().setAppName('{{cookiecutter.job_name}}')
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)

    main.etl_job(sc, sqlContext)
