from rest_framework_mongoengine.serializers import DocumentSerializer
from netflix_app.models.movies import movies
from .actors_serializer import actors_serializer
from .certificates_serializer import certificates_serializer
from .directors_serializer import directors_serializer
from .genres_serializer import genres_serializer

class movies_serializer(DocumentSerializer):
    cast = actors_serializer(many=True)
    certified = certificates_serializer()
    director = directors_serializer()
    genres = genres_serializer(many=True)
    class Meta:
        model = movies
        fields = '__all__'