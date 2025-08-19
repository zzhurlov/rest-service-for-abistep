# FastAPI + Postgres test-assignment for Abistep

This is a basic template for Django projects configured to use Docker Compose, Makefile, and PostgreSQL.

## Requirements

- FastAPI
- SQLAlchemy
- Alembic
- Docker
- Docker Compose
- GNU Make

## How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/zzhurlov/rest-service-for-abistep.git
   cd rest-service-for-abistep

2. Install all required packages

   ```bash
   poetry install --no-root --no-interaction --no-ansi


### Implemented Commands

* `make app` - up application and database/infrastructure
* `make app-logs` - follow the logs in app container
* `make app-down` - down application and all infrastructure
* `make app-shell` - go to contenerized interactive shell (bash)