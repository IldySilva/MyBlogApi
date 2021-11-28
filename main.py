from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import psycopg2
from model.authModels import CreateUserModel, LoginModel
from fastapi.responses import JSONResponse

import routes
import json

from model.userModel import UserModel
app = FastAPI()

database = psycopg2.connect(
    host='localhost', dbname="myblog", user="postgres", password="root")
cursor = database.cursor()


@app.post("/login")
def doLogin(loginModel: LoginModel):
    cursor.execute("SELECT id,name,phone FROM person WHERE phone = %s AND pwd = %s",
                   (loginModel.phone, loginModel.password))
    data = cursor.fetchall()
    if data:
        user = UserModel.fromJson(data[0])

        return JSONResponse(jsonable_encoder(user))

    else:
        return {"Wrong Username or password"}


@app.post("/createUser")
def createUser(data: CreateUserModel):
    try:
        cursor.execute("insert into person(name,phone,pwd) values (%s,%s,%s)",
                       (data.name, data.phone, data.password))
        return ({"sucesso": True, "mensagem": "Conta criada com sucesso"})

    except Exception as error:

        return ({"sucesso": False, "mensagem": error.args})
