from pyspark.sql  import SparkSession

if __name__ == '__main__':
    spark  = SparkSession.builder.appName("salesData").getOrCreate()

salesData = spark.sparkContext.textFile("sales.txt")
header = salesData.first()
noHeader = salesData.filter(lambda x:x != header)

deptSalesData = noHeader.map(lambda x: ((x.split(",")[0],x.split(",")[1],x.split(",")[3]),int(x.split(",")[2])))
revSalesData = deptSalesData.mapValues(lambda x: (x,1)).map(lambda subStr: (subStr[0],(subStr[1][1],subStr[1][0]))).reduceByKey(lambda x,y :(x[0] + y[0], x[1] + y[1]))

for i in revSalesData.collect():
    print(i)
