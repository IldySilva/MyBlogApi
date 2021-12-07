from fastapi import FastAPI
import psycopg2
import routes
from psycopg2.extras import RealDictCursor

from model.authModels import CreateUserModel, LoginModel, PostModel
from model.postsModel import Post

from model.userModel import UserModel

app = FastAPI()


database = psycopg2.connect(
    host='localhost', dbname="myblog", user="postgres", password="root")
cursor = database.cursor(cursor_factory=RealDictCursor)


@app.post("/createPost")
def MakePost(postModel: PostModel):
    try:

        cursor.execute("insert into posts(title,content,personid)values (%s,%s,%s);",
                       (postModel.title, postModel.content, postModel.personid))
        database.commit()
        return ({"sucesso": False, "Mensagem": " Post Feito com sucesso"})

    except Exception as error:

        return ({"sucesso": False, "Mensagem": error.args})


@app.get("/")
def unreouted():
    return 'Simple  Blog API Using Python'


@app.get("/posts")
def getAllPosts():
    try:
        posts = []
        cursor.execute(
            "select  posts.title,posts.content,posts.id as postId,posts.dateInserted ,person.name as personName,person.id as personId from posts inner join person on(posts.personid=person.id)")
        data = cursor.fetchall()
        database.commit()
        print(data)
        if data:

            return data

    except Exception as error:
        return ({"sucesso": False, "mensagem": error.args})


@app.get("/posts/{userId}")
def getFromUser(userId):
    cursor.execute("select * from posts where personid=%s", userId)
    data = cursor.fetchall()
    database.commit()
    if data:
        return data

    else:
        return "Este usuário não Tem nenhum post"


@app.get("/userById/{id}")
def userById(id):
    try:
        cursor.execute("select name,id,phone from person where id=%s", (id))
        data = cursor.fetchall()
        database.commit()
        if data:
            return data

    except Exception as error:
        return error


@app.post("/login")
def doLogin(loginModel: LoginModel):
    cursor.execute("SELECT id,name,phone FROM person WHERE phone = %s AND pwd = %s",
                   (loginModel.phone, loginModel.password))
    data = cursor.fetchall()
    database.commit()
    if data:
        return data[0]

    else:
        return {"Wrong Username or password"}


@app.post("/createUser")
def createUser(data: CreateUserModel):
    try:
        cursor.execute("insert into person(name,phone,pwd) values (%s,%s,%s)",
                       (data.name, data.phone, data.password))
        database.commit()

        return ({"sucesso": True, "mensagem": "Conta criada com sucesso"})

    except Exception as error:
        return ({"sucesso": False, "mensagem": error.args})
