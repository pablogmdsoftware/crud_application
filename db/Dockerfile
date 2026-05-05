# Use official PostgreSQL image
FROM postgres:16

# Copy initialization scripts
# Any .sql or .sh files in this folder will run on first startup
COPY data /data/
COPY schema.sql /docker-entrypoint-initdb.d/01_schema.sql
COPY insert_data.sql /docker-entrypoint-initdb.d/02_insert_data.sql

# Expose PostgreSQL port
EXPOSE 5432