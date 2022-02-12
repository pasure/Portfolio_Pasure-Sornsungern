## Mini Project : Apache Spark Cluster with Hypervisor and Container

> :memo: **Note:** Proof of concept Project.

### 1. System Overview

&nbsp;&nbsp;&nbsp;&nbsp;The purpose of this mini project is to build Apache Spark cluster in standalone mode on Docker with a JupyterLab interface and processing data 1 million record flie (in csv format) with PySpark.

![Overview_Project_Spark](/assets/images/Spark-01.png)

---------------

### 2. Download the docker compose file from Docker Hub

> :memo: **Reference :** https://github.com/cluster-apps-on-docker/spark-standalone-cluster-on-docker#download-from-docker-hub-easier .

1. Install Ubuntu 20.04 LTS on Virtual Machine
2. Download the docker compose file

```
curl -LO https://raw.githubusercontent.com/cluster-apps-on-docker/spark-standalone-cluster-on-docker/master/docker-compose.yml
```
3. Start the cluster
```
docker-compose up
```
---------------

### 3. Check Status of Worker with Spark UI (localhost:4040)

![Overview_Project_Spark](/assets/images/Spark-02.png)

---------------

### 4. Run Apache Spark code using Jupyter notebooks with PySpark (localhost:8888)

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
raw_df = spark.read.format('csv').option('header','true').option('mode','DROPMALFORMED') \        # Read file .csv
.load('/opt/workspace/LoanStats_web.csv')

print("Number of Columns : ",len(raw_df.columns))                 # Count Columns
print("Before-Number of Row : ",f"{raw_df.count():,}")            # Count Row

raw_df = raw_df.dropDuplicates()       # Drop Duplicates Record

print("After-Number of Row : ",f"{raw_df.count():,}")             # Count Row after Drop Duplicates Record

raw_df.write.mode('overwrite').parquet("/opt/workspace/NewFile.parquet") # Save Data Frame to Parquet File

print("------ FINISHED ------")
```
```
spark.stop()  # Optional
```
---------------
### 5. Compare status of worker between Two workers and One single worker with Spark UI

![Overview_Project_Spark](/assets/images/Spark-03.png)

---------------

### 6. Compare Spark jobs of worker between Two workers and One single worker with Spark UI

![Overview_Project_Spark](/assets/images/Spark-04.png)

![Overview_Project_Spark](/assets/images/Spark-05.png)

---------------
### 7. Compare Completed Stages of worker between Two workers and One single worker with Spark UI

![Overview_Project_Spark](/assets/images/Spark-06.png)

![Overview_Project_Spark](/assets/images/Spark-07.png)

---------------

![Overview_Project_Spark](/assets/images/Spark-08.png)

---------------

### 8. Compare Event timeline of worker between Two workers and One single worker with Spark UI

![Overview_Project_Spark](/assets/images/Spark-09.png)

![Overview_Project_Spark](/assets/images/Spark-10.png)

---------------

### 9. Compare Aggregated Metrics of worker between Two workers and One single worker with Spark UI

![Overview_Project_Spark](/assets/images/Spark-11.png)

![Overview_Project_Spark](/assets/images/Spark-12.png)

---------------
### 10. Compare Memmory Usage and CPU times of worker between Two workers and One single worker with Jupyter Interface

![Overview_Project_Spark](/assets/images/Spark-13.png)

---------------
### 11. Stop the cluster
1. Stop the cluster by typing ```ctrl+c``` on the terminal
2. Run Docker Compose again to restart the cluster
```
docker-compose up
```
---------------
