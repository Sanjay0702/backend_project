from mongoengine import Document, fields
from .actors import actors
from .certificates import certificates
from .directors import directors
from .genres import genres

class movies(Document):
    movie_name = fields.StringField()
    duration = fields.StringField(max_length=5)
    cast = fields.ListField(fields.ReferenceField(actors))
    description = fields.StringField()
    certified = fields.ReferenceField(certificates)
    release_year = fields.IntField()
    director = fields.ReferenceField(directors)
    genres = fields.ListField(fields.ReferenceField(genres))
    languages = fields.ListField(fields.StringField())
    rating = fields.StringField()
