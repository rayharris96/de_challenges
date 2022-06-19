-- Create table and load the table into Postgres database
-- Table type is varchar and null to account for dirty datasets
CREATE TABLE dataset1(
    name VARCHAR NULL,
    price VARCHAR NULL
);

CREATE TABLE dataset2(
    name VARCHAR NULL,
    price VARCHAR NULL
);

-- Copy dataset from raw csv
COPY dataset1 FROM '/var/lib/postgresql/csvs/dataset1.csv' WITH (FORMAT csv);
COPY dataset2 FROM '/var/lib/postgresql/csvs/dataset2.csv' WITH (FORMAT csv);
