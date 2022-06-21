# Section 2: Databases

## Problem Solutions
The Entity Relationship Diagram can be found in ERD.png

I have designed the tables into facts and dimensions. The tables in the database follows the third normal form. Third normal form (3NF) is a database schema design approach for relational databases which uses normalizing principles to reduce the duplication of data, avoid data anomalies, ensure referential integrity, and simplify data management.

The solution for this section consists of the following steps:
- ```make up``` calls a docker-compose function, which builds a Postgres image from the Dockerfile instructions
- It runs a database initialization code from `pg_init/init.sql`. This is where the DDL for the tables are set.
- Docker compose then mount the volume to persist data in the local host
- Assuming that the tables are populated over time, one can query the data based on the specified questions. The SQL query to address the questions can be found in `query/query1_customer_spending.sql` and `query/query2_car_sales.sql`
- ```make down``` to stop and clear the running containers

