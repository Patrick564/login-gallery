from fastapi import Form
from fastapi.utils import Optional


class UserData:
    def __init__(
        self,
        username: str = Form(...),
        email: Optional[str] = Form(None),
        password: str = Form(...),
        active: Optional[bool] = Form(None),
    ):
        self.username = username
        self.email = email
        self.password = password
        self.active = active
