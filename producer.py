from requests import get
from kafka import KafkaProducer
import json
import time

# Define the Kafka server properties
kafka_server = 'localhost:9092'
topic_name = 'bitcoin_prices'


# Initialize Kafka producer
def connect_kafka_producer():
    producer = None
    try:
        producer = KafkaProducer(bootstrap_servers=kafka_server,
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    except Exception as ex:
        print('Exception while connecting Kafka')
    finally:
        return producer


def get_price():
    URL = 'https://production.api.coindesk.com/v2/tb/price/ticker?assets=BTC'
    result = get(URL)
    json_data = result.json()
    btc_data = json_data['data']['BTC']
    price = btc_data['ohlc']['c']
    return price


# Function to send data to Kafka topic
def send_to_kafka(producer_instance, price):
    try:
        producer_instance.send(topic_name, value={"bitcoin_price": price})
        producer_instance.flush()
    except Exception as ex:
        print('Exception in publishing prices')
        print(str(ex))


if __name__ == "__main__":
    while True:
        bitcoin_price = get_price()
        producer = connect_kafka_producer()
        send_to_kafka(producer, bitcoin_price)
        print("Bitcoin Price:", bitcoin_price)
        time.sleep(10)  # Fetch data every 10 seconds
