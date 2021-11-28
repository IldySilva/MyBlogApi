from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import psycopg2
from model.loginModel import LoginModel

from fastapi.responses import JSONResponse
import json

from model.userModel import UserModel
app = FastAPI()


database = psycopg2.connect(
    host='localhost', dbname="myblog", user="postgres", password="root")
cursor = database.cursor()


@app.post("/login")
def makeLogin(loginModel: LoginModel):
    cursor.execute("SELECT * FROM person WHERE phone = %s AND pwd = %s",
                   (loginModel.phone, loginModel.password))
    data = cursor.fetchall()
    if data:
        user = UserModel.fromJson(data[0])

        return JSONResponse(jsonable_encoder(user))

    else:
        return {"Wrong Username or password"}
