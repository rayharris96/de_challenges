# Section 1: Data Pipelines

## Instructions
The objective of this section is to design and implement a solution to process a data file on a regular interval (e.g. daily). Assume that there are 2 data files dataset1.csv and dataset2.csv, design a solution to process these files, along with the scheduling component. The expected output of the processing task is a CSV file including a header containing the field names.

You can use common scheduling solutions such as cron or airflow to implement the scheduling component. You may assume that the data file will be available at 1am everyday. Please provide documentation (a markdown file will help) to explain your solution.

Processing tasks:

Split the name field into first_name, and last_name
Remove any zeros prepended to the price field
Delete any rows which do not have a name
Create a new field named above_100, which is true if the price is strictly greater than 100
Note: please submit the processed dataset too.

## Problem Solutions
The solution I have implemented consists of the following steps:
- Dockerized airflow and postgres containers to load the data and orchestrate scheduling of tasks
- Raw data is loaded at docker compose instance up into Postgres container. To start, type ```make up```
- Once Airflow is running, one can access the webserver via localhost:8080. Username and password is airflow and airflow
- Inside the DAG, there are two tasks - 'transform' and 'load'.
- Transformation task reads the sql code in `dags/sql` and applies transformation to a new table
- Save task executes bash command in `dags/scripts` and then saves the transformed table to a target destination
- The transformed data is saved at 'transformed_data' folder
- ```make down``` to stop and clear the running containers
