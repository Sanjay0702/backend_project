from rest_framework_mongoengine.viewsets import ModelViewSet
from netflix_app.serializers.genres_serializer import genres_serializer
from netflix_app.models.genres import genres
from rest_framework.parsers import JSONParser
from netflix_app.global_service.save_documents import save_documents
from netflix_app.global_service.get_document import get_document
from django.http import JsonResponse

class genres_viewset(ModelViewSet):
    lookup_field = "id"
    serializer_class = genres_serializer
    queryset = genres.objects