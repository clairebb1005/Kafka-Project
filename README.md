# Kafka-Project
A project is underway to implement Kafka-Python, a client designed for the Apache Kafka distributed stream processing system, to stream BitCoin price and to use Apache Spark for real-time price analytics.

## Install Spark
1. Go to official website [Spark](https://spark.apache.org/downloads.html) and and extract it in a new empty folder`C:\Spark`.

2. Create a foder `C:\Hadoop` and copy the `bin` file with your specific Hadoop version from this [repository](https://github.com/cdarlint/winutils/tree/master).

3. Download [Java](https://www.java.com/en/download/) if not yet installed.

4. Set `SPARK_HOME`as`C:\Spark\spark-3.5.0-bin-hadoop3`, `Hadoop`as`C:\Hadoop` , `JAVA_HOME`as`C:\Program Files\Java\jre-1.8`, and `SPARK_LOCAL_IP`as`127.0.0.1` for system variables. 

5. Set paths in system environment: `%SPARK_HOME%\bin` and `%HADOOP_HOME%\bin`.

6. Use `C:\Spark\spark-3.5.1-bin-hadoop3\bin\spark-shell` command in command prompt Window while running in administrator mode.

7. If you see Spark logo appears, then you successfully installed it.

## Test Spark
1. Open a web browser and navigate to http://localhost:4040/. An Apache Spark shell Web UI will show up.
2. To test Spark on command prompt, execute:
   * `val data = List("Test")`
   * `var t = sc.parallelize(data)`: will return `t: org.apache.spark.rdd.RDD[String] = ParallelCollectionRDD[0] at parallelize at <console>:24`.
   * `t.collect()`: will return `res0: Array[String] = Array(Test)`.

## Install Kafka
1. Go to [Kafka](https://kafka.apache.org/downloads) and click on Binary downloads.
2. Extract the zipped file into a new created empty folder `C:\Kafka`.
3. Go to `config` folder and choose:
   * zookeeper.properties file and change `dataDir` to `dataDir=C:/Kafka/kafka_2.13-3.7.0/zookeeper-data`.
   * server.properties file and change `log.dirs` to `log.dirs=C:/Kafka/kafka_2.13-3.7.0/kafka-logs `.

## Use Kafka
Open three seperate Command Prompt, all under `C:\Kafka\kafka_2.13-3.7.0` folder.
1. Execute Zoo-keeper `.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties`.
2. After Zoo-keeper is completely executed, execute Kafka Server `.\bin\windows\kafka-server-start.bat .\config\server.properties`.
3. Execute `.\bin\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic bitcoin-prices` to create a topic. It will return `Created topic bitcoin-prices` message.

Now, you can execute your `producer.py` file and it will scrape and stream Bitcoin Price in real-time.

## Setup Python
1. Use Anaconda to create a new environment for this project: `conda create -n kafka-project python=3.9`.
2. After installing all the dependencies in `requirement.txt`, add a environment variable `PYSPARK_PYTHON` with your desired Python path to your system environment.