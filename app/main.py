from fastapi import FastAPI
from app.db.database import engine, metadata, database
from app.models import database_model
from app.routes.user_routes import router as user_routes
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

metadata.create_all(bind=engine)
app.include_router(user_routes)

@app.on_event("startup")
async def connect_db():
    await database.connect()

@app.on_event("shutdown")
async def disconnect_db():
    await database.disconnect()