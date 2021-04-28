from sqlalchemy import Column, Integer, String, Boolean, Table

from db.settings import metadata


users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String, unique=True),
    Column('is_active', Boolean, default=True),
    Column('email', String, default='empty'),
    Column('password', String)
)
