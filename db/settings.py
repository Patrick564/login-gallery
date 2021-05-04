from os import getenv

from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

from databases import Database

load_dotenv('.env/.env')

metadata = MetaData()
database = Database(getenv('DATABASE_URL'))
engine = create_engine(getenv('DATABASE_URL'))

metadata.create_all(engine)
