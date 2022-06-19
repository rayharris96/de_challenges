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
