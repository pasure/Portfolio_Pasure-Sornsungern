## Mini Project : Apache Spark Cluster with Hypervisor and Container

> :memo: **Note:** Proof of concept Project.

### 1. System Overview

&nbsp;&nbsp;&nbsp;&nbsp;The purpose of this mini project is to build Apache Spark cluster in standalone mode on Docker with a JupyterLab interface and processing data 1 million record flie (in csv format) with PySpark.

![Overview_Project_Spark](/assets/images/Spark-01.png)

---------------

### 2. Download the docker compose file from Docker Hub

> :memo: **Reference :** https://github.com/cluster-apps-on-docker/spark-standalone-cluster-on-docker#download-from-docker-hub-easier .

1. Download the docker compose file

```
curl -LO https://raw.githubusercontent.com/cluster-apps-on-docker/spark-standalone-cluster-on-docker/master/docker-compose.yml
```
2. Start the cluster
```
docker-compose up
```	
3. Run Apache Spark code using Jupyter notebooks with PySpark
```
%load_ext memory_profiler
```
```
from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.\
        builder.\
        appName("pyspark-notebook").\
        master("spark://spark-master:7077").\
        config("spark.executor.core", "1").\
        getOrCreate()
```
```
%%time
%%memit
raw_df = spark.read.format('csv').option('header','true').option('mode','DROPMALFORMED') \
.load('/opt/workspace/LoanStats_web.csv')

print("Number of Columns : ",len(raw_df.columns))
print("Before-Number of Row : ",f"{raw_df.count():,}")

raw_df = raw_df.dropDuplicates()

print("After-Number of Row : ",f"{raw_df.count():,}")

raw_df.write.mode('overwrite').parquet("/opt/workspace/NewFile.parquet")

print("------ FINISHED ------")
```
```
spark.stop()
```
4. Stop the cluster by typing ```ctrl+c``` on the terminal
5. Run step 3 to restart the cluster


&nbsp;&nbsp;&nbsp;&nbsp;

---------------

### 3. Check Status of Worker with Spark UI

![Overview_Project_Spark](/assets/images/Spark-02.png)
