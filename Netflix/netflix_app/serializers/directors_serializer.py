from rest_framework_mongoengine.serializers import DocumentSerializer
from netflix_app.models.directors import directors

class directors_serializer(DocumentSerializer):
    class Meta:
        model = directors
        fields = ['name']