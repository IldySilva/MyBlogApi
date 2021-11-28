from pydantic import BaseModel


class Post(BaseModel):
    content = ""
    title = ""
    id = ""
    personid = ""

    def __init__(self, content, title, personid, id="") -> None:
        self.content = str(content)
        self.title = title
        self.personid = personid
        self.id = id

    def fromJson(json):
        return Post(id=json[0], content=json[1], title=json[2], personid=json[3])
