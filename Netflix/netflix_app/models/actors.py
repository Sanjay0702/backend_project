from mongoengine import Document,fields

class actors(Document):
    name = fields.StringField()
    age = fields.IntField(min_value=0)