from rest_framework_mongoengine.serializers import DocumentSerializer
from netflix_app.models.certificates import certificates

class certificates_serializer(DocumentSerializer):
    class Meta:
        model = certificates
        fields = ['certificate_name']