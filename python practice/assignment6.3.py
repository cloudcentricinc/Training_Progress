from pyspark.sql import SparkSession

if __name__ == '__main__' :
    spark = SparkSession.builder .appName("assignment_6_2").getOrCreate()


rawtxtFile = spark.sparkContext.textFile("orders.txt")
header = rawtxtFile.first()
noheader = rawtxtFile.filter(lambda x:x != header)
conditionOrders = noheader.filter(lambda x: x.split(",")[2] in ('2568', '256', '9842','9503'))

for c in conditionOrders.collect():
    print(c)