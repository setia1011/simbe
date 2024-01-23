### SIMBE
A blueprint of a SIMPLE BACKEND (Simbe) with the latest version of FastAPI, Pydantic, SQLAlchemy and Alembic.

### Venv
To create a virtual environment: `virtualenv venv`\
More: https://virtualenv.pypa.io/en/latest/

### Libraries
To install libraries: `pip install -r install.txt`

### .env
Example:

PROJECT_NAME=simbe\
BACKEND_CORS_ORIGINS=[] \
MYSQL_ROOT_PASSWORD= \
MYSQL_USER= \
MYSQL_PASSWORD= \
MYSQL_HOST= \
MYSQL_PORT= \
MYSQL_DATABASE= \
JWT_SECRET= \
JWT_ALGORITHM=HS256 \
SMTP_USERNAME= \
SMTP_PASSWORD= \
SMTP_HOST=smtp.gmail.com \
SMTP_PORT=465

### Database
To generate queries: `alembic revision --autogenerate`\
To execute generated queries: `alembic upgrade head`

### Run
On the terminal, inside root directory, execute: `python run.py`

### Author
Setia\
https://github.com/setia1011 \
https://techack.id \
https://codex.id