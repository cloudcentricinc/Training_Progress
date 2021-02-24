from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Countframe').getOrCreate()

readtxtFile = spark.read.csv("orders.txt")


noHeader= readtxtFile.first()

withoutheader  = readtxtFile.filter(lambda x:x != noheader)

filterDF  = withoutheader.filter(lambda x: x.split(",")[3] == "CLOSED")
                                            # x.split(",")[3] == "ON_HOLD" or
                                            # x.split(",")[3] == "COMPLETE" or
                                            # x.split(",")[3] == "PENDING_PAYMENT")


filterdf.show()