from rest_framework_mongoengine.viewsets import ModelViewSet
from netflix_app.serializers.actors_serializer import actors_serializer
from netflix_app.models.actors import actors
from rest_framework.parsers import JSONParser
from netflix_app.global_service.save_documents import save_documents
from netflix_app.global_service.get_document import get_document
from django.http import JsonResponse

class actors_viewset(ModelViewSet):
    lookup_field = "id"
    serializer_class = actors_serializer
    queryset = actors.objects