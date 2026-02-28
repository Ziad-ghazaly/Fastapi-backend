# FastAPI Backend – Shipment Management

This is a backend system built with **FastAPI** and **PostgreSQL** to manage shipments. It demonstrates API development, database integration, and production-ready backend workflows.

## Features

- Create, read, update, and delete shipments (`CRUD`)  
- Validates shipment data with **Pydantic / SQLModel** schemas  
- Tracks shipment status (`placed`, `in_transit`, `delivered`, `pending`)  
- Calculates estimated delivery date automatically for new shipments  
- Asynchronous database access with **SQLAlchemy / SQLModel** connected to **PostgreSQL**  
- Dependency injection using FastAPI’s `Depends`  

## Tech Stack

- Python 3  
- FastAPI  
- SQLModel & SQLAlchemy (async)  
- **PostgreSQL** (database)  
- Pydantic for validation  

## Project Structure

app/  
├── api/  
│   ├── router.py           # FastAPI routers  
│   └── schemas/           # Pydantic schemas  
├── database/  
│   ├── models.py           # SQLModel shipment models  
│   └── session.py          # DB engine & session dependency  
├── config.py               # Environment & DB settings  
└── main.py                 # FastAPI app entrypoint  

## Setup

1. Clone the repository:

```
git clone https://github.com/Ziad-ghazaly/Fastapi-backend.git
cd Fastapi-backend/app
```

2. Create and activate a virtual environment:

```
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Install dependencies manually:

```
pip install fastapi sqlmodel sqlalchemy asyncpg uvicorn
```

4. Create a `.env` file in the project root with PostgreSQL credentials:

```
POSTGRESQL_USER=your_user
POSTGRESQL_PASSWORD=your_password
POSTGRESQL_SERVER=localhost
POSTGRESQL_PORT=5432
POSTGRESQL_DB=fastapi_db
```

5. Make sure PostgreSQL is running and the database exists.

6. Start the FastAPI server:

```
uvicorn main:app --reload
```

7. Open API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Endpoints

| Method | Path       | Description                     |
|--------|------------|---------------------------------|
| GET    | /shipment/ | Retrieve a shipment by ID       |
| POST   | /shipment/ | Add a new shipment              |
| PATCH  | /shipment/ | Update an existing shipment     |
| DELETE | /shipment/ | Delete a shipment by ID         |

## Author

**Ziad Ghazaly** – [GitHub](https://github.com/Ziad-ghazaly) | [LinkedIn](https://www.linkedin.com/in/ziadghazaly)
