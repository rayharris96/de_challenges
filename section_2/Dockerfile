FROM postgres
WORKDIR /docker-entrypoint-initdb.d
ADD pg_init/init.sql /docker-entrypoint-initdb.d
EXPOSE 5432
