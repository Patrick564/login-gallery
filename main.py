from fastapi import FastAPI

from routes import home, login, logout, register

app = FastAPI()

app.include_router(home.router, prefix='/api/v1')
app.include_router(login.router, prefix='/api/v1/login')
app.include_router(logout.router, prefix='/api/v1/logout')
app.include_router(register.router, prefix='/api/v1/register')
