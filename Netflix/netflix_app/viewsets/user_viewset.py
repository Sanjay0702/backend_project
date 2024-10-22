from rest_framework_mongoengine.viewsets import ModelViewSet
from netflix_app.serializers.user_serializer import user_serializer
from netflix_app.models.user_details import user_details
from rest_framework.parsers import JSONParser
from netflix_app.global_service.save_documents import save_documents
from netflix_app.global_service.get_document import get_document
from django.http import JsonResponse

class user_viewset(ModelViewSet):
    lookup_field = "id"
    serializer_class = user_serializer
    queryset = user_details.objects