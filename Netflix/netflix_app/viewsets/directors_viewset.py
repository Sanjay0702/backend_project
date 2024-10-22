from rest_framework_mongoengine.viewsets import ModelViewSet
from netflix_app.serializers.directors_serializer import directors_serializer
from netflix_app.models.directors import directors
from rest_framework.parsers import JSONParser
from netflix_app.global_service.save_documents import save_documents
from netflix_app.global_service.get_document import get_document
from django.http import JsonResponse

class directors_viewset(ModelViewSet):
    lookup_field = "id"
    serializer_class = directors_serializer
    queryset = directors.objects