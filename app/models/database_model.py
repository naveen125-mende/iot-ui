from sqlalchemy import Table, Column, String,Boolean,DateTime
from app.db.database import metadata

users = Table(
    "users",
    metadata,
    Column("username", String(50), primary_key=True),
    Column("email", String(100)),
    Column("otp",String(6)),
    Column("generated_at",DateTime)
)

connected_users = Table(
    "connected_users",
    metadata,
    Column("Device Name", String(50)),
    Column("Device ID", String(50), primary_key=True),
    Column("Connected-Date", String(50)),
    Column("Data Usage", String(50)),
    Column("Status", Boolean, default=True),
)

