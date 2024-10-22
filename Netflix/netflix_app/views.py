from django.shortcuts import render
from netflix_app.models.profiles import profile
from rest_framework.parsers import JSONParser
from netflix_app.global_service.save_documents import save_documents
from netflix_app.global_service.get_document import get_document
from netflix_app.global_service.update_documents import update_documents
from netflix_app.global_service.list_documents import list_documents
from netflix_app.serializers.movies_serializer import movies_serializer
from netflix_app.models.user_details import user_details
from netflix_app.models.movies import movies 
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
# @api_view(['GET', 'POST'])
def login(request):
    json_request = JSONParser().parse(request)
    user_info = json_request["username"]
    password = json_request["pass"]
    # print(user_info,password)
    if user_info.isdigit():
        user_obj = get_document(user_details.objects,{'phone_number' : user_info })
    else:
        user_obj = get_document(user_details.objects,{'email' : user_info })
    dict = {}
    dict["Status"] = False
    if user_obj == None:
        dict["error"] = "User Not Found"
    if user_obj.password == password:
        dict ={
            "Status" : True,
            "id": str(user_obj.id)
        } 
    else:
        dict ={
            "error" : "Incorrect Password",
            "Status" : False
        } 
    return JsonResponse(dict, safe = True)
    

@csrf_exempt
def signup(request):
    json_request = JSONParser().parse(request)
    email = json_request['email']
    user_obj = get_document(user_details.objects,{'email':email})
    print(user_obj)
    dict = {}
    if user_obj == None:
        profile_obj = get_document(profile.objects,{'name': "childern"})
        json_request['profiles']=[profile_obj.id]
        new_doc = save_documents(user_details, json_request)
        dict["Status"] = True,
        dict["id"] = str(new_doc.id)
    else:
        dict = {
            "error" : "Email is already exits",
            "Status" : False
        } 
    return JsonResponse(dict, safe = False)

@csrf_exempt
def home(request):
    dict = []
    json_request = JSONParser().parse(request)
    search = json_request['search']
    if search == "":
        movies_object = list_documents(movies.objects,{})
    else:
        movies_object = list_documents(movies.objects,{"movie_name__iregex": search})
    
    if len(movies_object) == 0:
        return JsonResponse("No related movies",safe=False)
    
    serialized_data = movies_serializer(movies_object,many=True).data
    for data in serialized_data:
        dict.append({'movie_name' : data['movie_name'], "id" : data['id']})
    return JsonResponse(dict,safe=False)

@csrf_exempt       
def profiles(request):
    json_request = JSONParser().parse(request)
    profile_name = json_request['name']
    user_id = json_request['id']
    pro_obj = save_documents(profile, {'name': profile_name})
    new_profile = update_documents(user_details.objects, {'id':user_id},{'push__profiles': pro_obj.id})
    dict ={
        "error" : "No error",
        "Status" : True
    }
    return JsonResponse(dict, safe = False)