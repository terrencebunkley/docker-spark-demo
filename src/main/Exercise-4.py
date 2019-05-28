import Util

from pyspark.sql import SparkSession
from datetime import date

import pyspark.sql.functions as F
import pyspark.sql.types as T

if __name__ == "__main__":
    exerciseNum = 4
    print(Util.loggingSeparator)
    print("Exercise %i" % exerciseNum)

    # Create Spark Instance
    spark = SparkSession \
        .builder \
        .appName("Exercise %i" % exerciseNum) \
        .getOrCreate()

    # Location of CSV File
    filePath = "/docker-spark-demo/data/crimes/Crimes_-_One_year_prior_to_present.csv"


    def get_DD_MM_YYYY(col):
        return col.split(' ')[0]


    getDate = F.UserDefinedFunction(get_DD_MM_YYYY, T.StringType())

    # Load  DataFrame From the CSV
    df = spark.read.load(filePath, format="csv", sep=",", inferSchema="true", header="true").cache()

    # Add columns to Dataframe  DATE_AS_STRING
    df = df.withColumn('DATE_AS_STRING', getDate('DATE  OF OCCURRENCE'))

    # Add Date object to the Dataframe
    df = df.withColumn('Date', F.to_date('DATE_AS_STRING', 'MM/dd/yyyy'))

    df.filter((df['Date'] > date(2018, 3, 20)) & (df['Date'] < date(2018, 6, 21))) \
        .groupBy(" LOCATION DESCRIPTION").count().sort("count", ascending=False).show(n=100, truncate=False)

    print(Util.loggingSeparator)

    spark.stop()
