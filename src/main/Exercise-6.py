import Util

from pyspark.sql import SparkSession

import pyspark.sql.functions as F
import pyspark.sql.types as T

if __name__ == "__main__":
    exerciseNum = 6
    print(Util.loggingSeparator)
    print("Exercise %i" % exerciseNum)

    # Create Spark Instance
    spark = SparkSession \
        .builder \
        .appName("Exercise %i" % exerciseNum) \
        .getOrCreate()

    # Location of CSV File
    filePath = "/docker-spark-demo/data/mobile_data/MobileSampleData.csv"

    # Load  DataFrame From the CSV
    df = spark.read.load(filePath, format="csv", sep=",", inferSchema="true", header="true").cache()

    df.groupBy("DevicePlatform").count().sort("count", ascending=False).show(n=100, truncate=False)

    df.drop('QueryTime', 'SessionId', 'SessionPageViewOrder', 'Market').drop_duplicates()\
        .write.partitionBy("DevicePlatform").save("/docker-spark-demo/output/json", "json")

    print(Util.loggingSeparator)

    spark.stop()
