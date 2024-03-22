from pyspark.sql import SparkSession
from pyspark.sql.functions import window, avg
from pyspark.sql.types import StructType, TimestampType, DoubleType
from kafka import KafkaConsumer
import json
from datetime import datetime


# Create a SparkSession
spark = SparkSession.builder \
    .appName("BitcoinPriceAnalytics") \
    .getOrCreate()

# Define the schema for Bitcoin price data
schema = StructType().add("timestamp", TimestampType()).add("bitcoin_price", DoubleType())

# Create a Kafka consumer
consumer = KafkaConsumer('bitcoin-prices', bootstrap_servers='localhost:9092', auto_offset_reset='latest')

# Create a DataFrame to store streaming data
df = spark.createDataFrame([], schema)

# Process each message from Kafka
for message in consumer:
    data = json.loads(message.value.decode('utf-8'))
    timestamp = datetime.fromtimestamp(data['timestamp'])
    bitcoin_price = data['bitcoin_price']
    df = df.union(spark.createDataFrame([(timestamp, bitcoin_price)], schema))

    # Perform windowed aggregation (e.g., 10 minutes windows)
    windowed_df = df.groupBy(window(df.timestamp, "10 minute")).agg(avg("bitcoin_price").alias("mean_price"))
    windowed_df.show()

# Start the Spark session
spark.stop()