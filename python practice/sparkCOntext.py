from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]").appName("spark demo").getOrCreate()

rdd=spark.sparkContext.parallelize([1,2,3,4,5])

rdd.count()
withoutheader  = readtxtFile.filter(lambda x:x !=header)