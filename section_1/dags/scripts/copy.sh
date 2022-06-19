#!/usr/bin/env bash
source=$1

docker exec -it -u postgres containerdb psql -d database -c "COPY (SELECT first_name,last_name,price,above_100 FROM $source) TO STDOUT DELIMITER ',' CSV HEADER" > section_1/transformed_data/$source.csv
echo "Save completed"
