from datetime import timedelta
from pydantic import BaseModel


class LoginModel(BaseModel):
    phone: str
    password: str


class CreateUserModel(BaseModel):
    phone: str
    password: str
    name: str


class PostModel(BaseModel):
    content: str
    title: str
    personid: str
