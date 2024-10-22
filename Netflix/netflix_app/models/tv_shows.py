from mongoengine import Document, fields
from mongoengine import Document, fields
from .actors import actors
from .certificates import certificates
from .directors import directors
from .genres import genres

class tv_shows(Document):
    show_name = fields.StringField()
    no_of_seasons = fields.IntField(min_value = 0)
    cast = fields.ListField(fields.ReferenceField(actors))
    description = fields.StringField()
    certified = fields.ReferenceField(certificates)
    release_year = fields.IntField()
    director = fields.ReferenceField(directors)
    languages = fields.ListField(fields.StringField())
    rating = fields.StringField()
