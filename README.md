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
