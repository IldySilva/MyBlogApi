from pydantic import BaseModel


class LoginModel(BaseModel):
    phone: str
    password: str


class CreateUserModel(BaseModel):
    phone: str
    password: str
    name: str


class PostModel(BaseModel):
    content = ""
    title = ""
    personid = ""
