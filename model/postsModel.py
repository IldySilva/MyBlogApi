class Post:
    content = ""
    title = ""
    id = ""
    personid = ""

    def fromJson(json):
        return Post(id=json[0], content=json[1], title=json[2], personid=json[3])

    def __init__(self, content, title, id, personid) -> None:
        self.content = content
        self.title = title
        self.personid = personid
        self.id = id
