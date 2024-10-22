from mongoengine import Document, fields

class profile(Document):
    name = fields.StringField()
