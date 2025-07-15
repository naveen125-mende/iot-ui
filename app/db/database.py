from dotenv import load_dotenv
from pathlib import Path
import os

# 👇 Adjust this to point to app/.env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv("DB_URL")
if not DATABASE_URL:
    raise ValueError("DB_URL not set in .env")
from databases import Database
from sqlalchemy import create_engine, MetaData

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL.replace("aiomysql", "pymysql"))
metadata = MetaData()
