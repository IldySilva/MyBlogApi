class UserModel:
    phone: str
    pwd: str
    id: str
    name: str

    def __init__(self, id, name, phone, pwd="") -> None:
        self.phone = str(phone)
        self.pwd = str(pwd)
        self.id = str(id)
        self.name = name

    def fromJson(json):
        return UserModel(id=json[0], name=json[1], phone=json[2])

    def toJson(self):
        return ({
            "id": str(self.id),
            "phone": self.phone,
            "nome": self.name,

        })
