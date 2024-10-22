from rest_framework_mongoengine.serializers import DocumentSerializer
from netflix_app.models.user_details import user_details

class user_serializer(DocumentSerializer):
    class Meta:
        model = user_details
        exclude = ['id']