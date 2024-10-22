from mongoengine import Document, fields
from .profiles import profile
class user_details(Document):
    GENDER = {
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    }
    name = fields.StringField(max_length = 255)
    email = fields.EmailField(unique = True)
    phone_number = fields.StringField(max_length = 10, min_length = 10, unique = True)
    password = fields.StringField(max_length = 255)
    gender = fields.StringField(choices = GENDER)
    date_of_birth = fields.DateField()
    age = fields.IntField(min_value = 0)
    profiles = fields.ListField(fields.ReferenceField(profile))