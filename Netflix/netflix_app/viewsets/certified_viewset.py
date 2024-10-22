from rest_framework_mongoengine.viewsets import ModelViewSet
from netflix_app.serializers.certificates_serializer import certificates_serializer
from netflix_app.models.certificates import certificates
from rest_framework.parsers import JSONParser
from netflix_app.global_service.save_documents import save_documents
from netflix_app.global_service.get_document import get_document
from django.http import JsonResponse

class certified_viewset(ModelViewSet):
    lookup_field = "id"
    serializer_class = certificates_serializer
    queryset = certificates.objects