from mongoengine import Document, fields

class directors(Document):
    name = fields.StringField(max_length = 255)
    age = fields.IntField(min_value = 0)

