from mongoengine import Document, fields

class genres(Document):
    movie_genres = fields.StringField()