from rest_framework_mongoengine.serializers import DocumentSerializer
from netflix_app.models.actors import actors

class actors_serializer(DocumentSerializer):
    class Meta:
        model = actors
        fields = ['name']