from rest_framework_mongoengine.viewsets import ModelViewSet
from netflix_app.serializers.movies_serializer import movies_serializer
from netflix_app.models.movies import movies
from rest_framework.parsers import JSONParser
from netflix_app.global_service.save_documents import save_documents
from netflix_app.global_service.get_document import get_document
from django.http import JsonResponse

class movies_viewset(ModelViewSet):
    lookup_field = "id"
    serializer_class = movies_serializer
    queryset = movies.objects

    def create(self, request):
        data1 = dict()
        json_request = JSONParser().parse(request)
        obj = save_documents(movies, json_request)
        serialized_data = self.serializer_class(obj).data
        data1["movie"] = serialized_data["movie_name"]
        data1["cast"] = serialized_data['cast']
        return JsonResponse(data1, safe=False)
    
    def list(self, request):
        queryset = self.queryset.filter()
        serializer = self.serializer_class(queryset, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)