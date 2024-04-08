## Mini Project : Data Pipeline with Apache Airflow

> :memo: **Note:** Proof of concept Project.

### 1. System Overview

&nbsp;&nbsp;&nbsp;&nbsp;The purpose of this mini project is to build Data Pipeline using Apache Airflow on Docker for import data from Public API, Extract-Transform-Load (ETL) data (in CSV and JSON format) with Pandas, import data into Microsoft SQL Server and then notice user via email (MailHog) when data pipeline succeeded.

![Overview_Project_Airflow](/assets/images/Airflow-Images-01.png)

![Overview_Project_Airflow](/assets/images/Airflow-Images-02.png)

---------------

### 2. Download the docker compose file from Airflow Website

> :memo: **Reference :** https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html .

1. Install Ubuntu 20.04 LTS on Virtual Machine
2. Download the docker compose file

```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.3/docker-compose.yaml'
```
3. Add the following to docker-compose.yml (for use MailHog)
```
services:
  mailhog:
    image: mailhog/mailhog:latest    
    ports:
      - 1025:1025
      - 8025:8025
```
4. Start the cluster
```
docker-compose up
```
---------------

### 3. Create table in Microsoft SQL Server

![Overview_Project_Airflow](/assets/images/Airflow-Images-03.png)

![Overview_Project_Airflow](/assets/images/Airflow-Images-04.png)

---------------

### 4. Create Python files

1. Create [demo_etl.py](https://github.com/pasure/Portfolio_Pasure-Sornsungern/blob/main/Mini%20Project%20:%20Data%20Pipelines%20with%20Apache%20Airflow/dags/demo_etl.py) (For specifying the DAG’s structure as code)

2. Create [functions.py](https://github.com/pasure/Portfolio_Pasure-Sornsungern/blob/main/Mini%20Project%20:%20Data%20Pipelines%20with%20Apache%20Airflow/dags/functions.py) (For contain python functions)

---------------

### 5. Configure necessary variable in Apache Airflow

![Overview_Project_Airflow](/assets/images/Airflow-Images-05.png)

---------------

### 6. Run Data pipeline with Apache Airflow

![Overview_Project_Airflow](/assets/images/Airflow-Images-06.png)

---------------

### 7. Monitor Data pipeline with Airflow UI

![Overview_Project_Airflow](/assets/images/Airflow-Images-07.png)

![Overview_Project_Airflow](/assets/images/Airflow-Images-08.png)

![Overview_Project_Airflow](/assets/images/Airflow-Images-09.png)

![Overview_Project_Airflow](/assets/images/Airflow-Images-10.png)

---------------

### 8. All Results

![Overview_Project_Airflow](/assets/images/Airflow-Images-11.png)

![Overview_Project_Airflow](/assets/images/Airflow-Images-12.png)

![Overview_Project_Airflow](/assets/images/Airflow-Images-13.png)

![Overview_Project_Airflow](/assets/images/Airflow-Images-14.png)

![Overview_Project_Airflow](/assets/images/Airflow-Images-15.png)

![Overview_Project_Airflow](/assets/images/Airflow-Images-16.png)

---------------
