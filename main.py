from fastapi import FastAPI
import mysql.connector 
import mysql
from model.loginModel import LoginModel
import json

from model.userModel import UserModel


database=mysql.connector.connect(host="127.0.0.1",user="root",database="myblog")
cursor=database.cursor()
app=FastAPI()



@app.post("/login")
def makeLogin(loginModel: LoginModel):
    cursor.execute("SELECT * FROM usuarios WHERE phone = %s AND pwd = %s", (loginModel.phone, loginModel.password)) 
    data= cursor.fetchall()
    if data :
       user=UserModel.fromJson(data[0])
  
       return user.toJson()
      
    else:
        return {"Wrong Username or password"}





