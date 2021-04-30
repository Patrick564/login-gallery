from fastapi import FastAPI

from routes import login, logout, register, get_user

from core.events import startup_connection, shutdown_connection

app = FastAPI()

app.add_event_handler('startup', startup_connection)
app.add_event_handler('shutdown', shutdown_connection)

app.include_router(get_user.router, prefix='/api/v1/user')
app.include_router(login.router, prefix='/api/v1/login')
app.include_router(logout.router, prefix='/api/v1/logout')
app.include_router(register.router, prefix='/api/v1/register')
