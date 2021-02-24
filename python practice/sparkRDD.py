from pyspark import SparkConf
from pyspark import SparkContext

if __name__ == '__main__' :
    conf =SparkConf()
    sc= SparkContext(conf = conf)


readtxtFile = sc.textFile("orders.txt")

header= readtxtFile.first()

withoutheader  = readtxtFile.filter(lambda x:x !=header)
filterRDD  = withoutheader.filter(lambda x: x.split(",")[3] == "CLOSED" or
                                            x.split(",")[3] == "ON_HOLD" or
                                            x.split(",")[3] == "COMPLETE" or
                                            x.split(",")[3] == "PENDING_PAYMENT")

rdd2 = filterRDD.map(lambda y: (y.split(",")[3], 1))
orderGroup = rdd2.reduceByKey(lambda a,b : a + b)
orderGroup.coalesce(1).saveAsTextFile("filterTxt")






