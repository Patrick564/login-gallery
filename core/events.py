from db.settings import database


async def startup_connection():
    await database.connect()


async def shutdown_connection():
    await database.disconnect()
