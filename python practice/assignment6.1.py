from pyspark.sql import SparkSession

if __name__ == '__main__':
    spark = SparkSession.builder .appName("assignemnt_6_1").getOrCreate()


txtFile = spark.sparkContext.textFile("orders.txt")
header = txtFile.first()
noheader = txtFile.filter(lambda x:x != header)
condOrders = ['CLOSED','COMPLETE','ON_HOLD','PENDING_PAYMENT']
condOrders2 = noheader.filter(lambda x: x.split(",")[3] in condOrders)
ordersCon = condOrders2.map(lambda y: (y.split(",")[3],1))
finalOrders = ordersCon.reduceByKey(lambda a, b : a + b)

for c in finalOrders.collect():
    print(c)

