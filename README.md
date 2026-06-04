# Task Manager API

A RESTful CRUD API built with **FastAPI** and **PostgreSQL** for managing users, projects, tasks, and task comments.

The application is containerized with Docker and can be started with a single command.

## Features

* User management
* Project management
* Task management
* Comments on tasks
* PostgreSQL database integration
* FastAPI automatic OpenAPI documentation
* Preloaded database with sample data for testing and development
* Dockerized environment for easy setup

---

## Technologies

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Docker
* Docker Compose

---

## Project Structure

```text
.
├── api/
├── db/
│   └── schema.png
├── .env/
├── docker-compose.yml
└── README.md
```

---

## Prerequisites

Before running the project, make sure you have installed:

* Docker
* Docker Compose

---

## Security Notice

⚠️ **Important**

Database credentials are currently stored in the `.env` file and are intended only for development purposes.

Before starting the application, update the values in the `.env` file with your own secure credentials.

Example:

```env
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=your_database
```

Failure to change these values may expose your database to unauthorized access.

---

## Running the Project

Start all services:

```bash
docker compose up -d
```

To verify the containers are running:

```bash
docker ps
```

---

## Service Ports

| Service     | Port |
| ----------- | ---- |
| FastAPI API | 8000 |
| PostgreSQL  | 5433 |

---

## API Documentation

FastAPI automatically generates interactive API documentation.

After starting the project, visit:

```text
http://localhost:8000/docs
```

From this interface you can:

* Explore available endpoints
* Execute requests directly from the browser
* Authenticate and test protected routes

---

## Authentication Note

⚠️ **Known Documentation Limitation**

In the Swagger UI authentication dialog (`/docs`), the login form indicates that a **username** should be used.

However, the API actually requires the user's **email address** for authentication.

Use:

```text
email + password
```

instead of:

```text
username + password
```

when obtaining or using authentication credentials.

---

## Database Schema

The database structure can be found in the `db` directory.

Schema diagrams are provided to help visualize the relationships between entities.

Main entities:

* Users
* Projects
* Tasks
* Comments

Typical relationships:

* A user can own multiple projects.
* A project contains multiple tasks.
* A task can contain multiple comments.
* Users can create comments on tasks.

Refer to the schema files inside the `db` folder for detailed table definitions and relationships.

---

## Sample Data

The database is populated with sample/mock data by default.

This allows you to:

* Test endpoints immediately
* Explore relationships between entities
* Develop frontend applications without creating initial records manually

---

## Development

To view logs:

```bash
docker compose logs -f
```

To stop the application:

```bash
docker compose down
```

To rebuild containers:

```bash
docker compose up --build -d
```

---

## API Overview

The API provides CRUD operations for:

### Users

* Create users
* Retrieve users
* Update users
* Delete users

### Projects

* Create projects
* Retrieve projects
* Delete projects

### Tasks

* Create tasks
* Retrieve tasks
* Update tasks
* Delete tasks

### Comments

* Create comments
* Retrieve comments
* Update comments
* Delete comments

For detailed request and response schemas, refer to the interactive documentation at `/docs`.

---

## License

This project is intended for educational and development purposes.
