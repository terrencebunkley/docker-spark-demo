import Util

from pyspark.sql import SparkSession

if __name__ == "__main__":
    exerciseNum = 3
    print(Util.loggingSeparator)
    print("Exercise %i" % exerciseNum)

    # Create Spark Instance
    spark = SparkSession \
        .builder \
        .appName("Exercise %i" % exerciseNum) \
        .getOrCreate()

    # Location of CSV File
    filePath = "/docker-spark-demo/data/crimes/Crimes_-_One_year_prior_to_present.csv"

    # Load  DataFrame From the CSV
    df = spark.read.load(filePath, format="csv", sep=",", inferSchema="true", header="true").cache()

    # Show Number of arrests and non arrests
    df.groupBy("ARREST").count().show()

    print(Util.loggingSeparator)

    spark.stop()
