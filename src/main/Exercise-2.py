import Util

from pyspark.sql import SparkSession

if __name__ == "__main__":
    exerciseNum = 2
    print(Util.loggingSeparator)
    print("Exercise %i" % exerciseNum)

    '''
    Exercise 2:
    We are going to load a CSV document and filter the data for the crimes listed as other offenses.
    '''
    # Create Spark Instance
    spark = SparkSession \
        .builder \
        .appName("SimpleCrimeCSVParser") \
        .getOrCreate()

    # Location of CSV File
    filePath = "/docker-spark-demo/data/crimes/Crimes_-_One_year_prior_to_present.csv"

    # Load  DataFrame From the CSV
    df = spark.read.load(filePath, format="csv", sep=",", inferSchema="true", header="true").cache()

    # We can use the 'filter' function to refine the data.
    # The 'show' method outputs this data to the console.
    df.filter(df[" PRIMARY DESCRIPTION"] == 'OTHER OFFENSE').show(50)

    print(Util.loggingSeparator)

    spark.stop()





