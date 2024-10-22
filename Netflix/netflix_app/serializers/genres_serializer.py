from rest_framework_mongoengine.serializers import DocumentSerializer
from netflix_app.models.genres import genres

class genres_serializer(DocumentSerializer):
    class Meta:
        model = genres
        fields = ['movie_genres']