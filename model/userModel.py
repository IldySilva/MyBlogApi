class UserModel:
    phone:str
    pwd:str
    id:str
    name:str

    def __init__(self,pwd,id,name,phone) -> None:
        self.phone=phone,
        self.pwd=pwd,
        self.id=id,
        self.name=name
        
    
    def fromJson(json):
        return UserModel(pwd=str(json[0]),name=json[2],id=json[3],phone=json[1])

    def toJson(self):
        return ({
        
          "pwd":self.pwd,
          "id":self.id,
          "phone":self.phone,
          "nome":self.name,

        })
    