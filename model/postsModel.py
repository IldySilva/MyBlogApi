
from pydantic import BaseModel
import json


class Post():
    content: str
    title: str
    id: str
    personid: str

    def __init__(self, content, title, personid, id="") -> None:
        self.content = str(content)
        self.title = str(title)
        self.personid = str(personid)
        self.id = id

    def fromJson(json):
        return Post(id=json[0], content=json[1], title=json[2], personid=json[3])

    def toJson(self):
        return json.dumps(self)
