#!/usr/bin/env bash
source=$1

docker exec -it -u postgres containerdb \
psql -d database -c "COPY (SELECT * FROM $source) TO STDOUT CSV" > section_1/temp/$source.csv
