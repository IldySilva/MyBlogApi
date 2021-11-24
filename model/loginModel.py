from pydantic import BaseModel

class LoginModel(BaseModel):
    phone:str
    password:str