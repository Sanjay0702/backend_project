from mongoengine import Document, fields

class certificates(Document):
    certificate_name = fields.StringField(max_length = 10)