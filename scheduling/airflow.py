from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from example_job import main

if __name__ == "__main__":
    conf = SparkConf().setAppName('example_etl')
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)

    main.etl_job(sc, sqlContext)
