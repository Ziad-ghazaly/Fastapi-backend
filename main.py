from contextlib import asynccontextmanager

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference


from app.database.session import create_db_and_tables


from app.api.router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()  # Ensure the database and tables are created at startup
    yield 
    print("Shutting down the application...")
    

app = FastAPI(lifespan=lifespan)

app.include_router(router)

@app.get("/scalar", include_in_schema=False)
def get_scalar():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="scalar API")
