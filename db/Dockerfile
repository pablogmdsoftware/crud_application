# Use official PostgreSQL image
FROM postgres:16

# Set environment variables
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase

# Copy initialization scripts
# Any .sql or .sh files in this folder will run on first startup
COPY schema.sql /docker-entrypoint-initdb.d/schema.sql

# Expose PostgreSQL port
EXPOSE 5432