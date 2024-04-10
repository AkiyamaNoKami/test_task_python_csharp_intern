from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("ProductCategoryAnalysis") \
    .getOrCreate()

products_df = spark.read.csv("products.csv", header=True, inferSchema=True)
categories_df = spark.read.csv("categories.csv", header=True, inferSchema=True)
joined_df = products_df.join(categories_df, products_df["product_id"] == categories_df["product_id"], "left_outer")
pairs_df = joined_df.select(products_df["product_name"], categories_df["category_name"])


products_without_categories_df = products_df.join(categories_df, products_df["product_id"] == categories_df["product_id"], "left_outer") \
    .filter(categories_df["category_id"].isNull()) \
    .select(products_df["product_name"])


pairs_df.show()
products_without_categories_df.show()
spark.stop()
