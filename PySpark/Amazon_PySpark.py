from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.sql.functions import sum, avg, max, min, mean, count, contains

def getRelatedProducts(cvs_data):
    conf = SparkConf().setAppName("Leer archivo cvs")
    sc = SparkContext.getOrCreate(conf=conf)
    amazon_rdd = sc.textFile(cvs_data)

    spark = SparkSession.builder.getOrCreate()

    headers = amazon_rdd.first()
    rdd = amazon_rdd.filter(lambda x: x != headers).map(lambda x: x.split(","))
    rdd_columns = rdd.map(lambda row: (int(row[0]), row[1], row[2], float(row[3]), row[4]))
    columns = headers.split(",")

    schema = StructType([
        StructField("ID", IntegerType(), False),
        StructField("Product_Name", StringType(), False),
        StructField("Link", StringType(), False),
        StructField("Price", FloatType(), False),
        StructField("Description", StringType(), False),
    ])

    df_with_schema = spark.createDataFrame(rdd_columns, schema=schema)

    product_name = input("What are you looking for? ")
    df = df_with_schema.filter(df_with_schema.Product_Name.contains(product_name))
    products = df.show(15)

    return products