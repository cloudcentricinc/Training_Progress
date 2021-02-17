from pyspark.sql import SparkSession
spark= SparkSession.builder.appName("starsequence").getOrCreate()

print(spark)
