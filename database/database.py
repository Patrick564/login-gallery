from sqlalchemy import create_engine, MetaData

from databases import Database


DATABASE_URL = 'postgresql://patrick:123456789@localhost/project1'  # noqa


metadata = MetaData()
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)

metadata.create_all(engine)
