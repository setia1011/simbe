### SIMBE
A blueprint of a SIMPLE BACKEND (Simbe) with the latest version of FastAPI, Pydantic, SQLAlchemy and Alembic

```
simbe
├── alembic
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── d3dadd4bff67_.py
├── alembic.ini
├── app
│   ├── core
│   │   ├── config.py
│   │   └── database.py
│   ├── main.py
│   ├── utils
│   └── v1
│       ├── api.py
│       ├── models
│       ├── routers
│       ├── schemas
│       └── services
├── venv
├── install.txt
├── LICENSE
├── README.md
├── requirements.txt
└── run.py
```

### Venv
To create a new python virtual environment: ```virtualenv venv```\
To activate, in Linux or Mac: ```source venv/bin/activate```\
Or in Windows: ```venv\Scripts\activate```

More: https://virtualenv.pypa.io/en/latest/

### Libraries
To install libraries: ```pip install -r install.txt```

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
To generate queries: ```alembic revision --autogenerate```\
To execute generated queries: ```alembic upgrade head```

### Run
On the terminal, inside root directory, execute: ```python run.py```

### Author
**Setia**\
setiadi1457@gmail.com\
https://github.com/setia1011

### References
https://fastapi.tiangolo.com \
https://docs.pydantic.dev/latest \
https://www.sqlalchemy.org \
https://alembic.sqlalchemy.org/en/latest