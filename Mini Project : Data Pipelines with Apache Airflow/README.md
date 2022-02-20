## Mini Project : Data Pipeline with Apache Airflow

> :memo: **Note:** Proof of concept Project.

### 1. System Overview

&nbsp;&nbsp;&nbsp;&nbsp;The purpose of this mini project is to build Data Pipeline using Apache Airflow on Docker for import data from Public API, Extract-Transform-Load (ETL) data (in CSV and JSON format) with Pandas, import data into Microsoft SQL Server and then notice user via email (MailHog) when data pipeline succeeded.

![Overview_Project_Spark](/assets/images/Airflow-Images-01.png)

![Overview_Project_Spark](/assets/images/Airflow-Images-02.png)

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
