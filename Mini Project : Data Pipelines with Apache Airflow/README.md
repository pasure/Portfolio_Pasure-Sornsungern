## Mini Project : Mini Project : Data Pipelines with Apache Airflow

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
