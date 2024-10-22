from django.urls import path
from rest_framework.routers import SimpleRouter
from .viewsets.user_viewset import user_viewset
from .viewsets.movie_viewset import movies_viewset
from .viewsets.genres_viewset import genres_viewset
from .viewsets.directors_viewset import directors_viewset
from .viewsets.certified_viewset import certified_viewset
from .viewsets.actors_viewset import actors_viewset

from .views import signup,login,home,profiles
routers = SimpleRouter()
routers.register("user_viewset", user_viewset, basename = "user_viewset")
routers.register("movies_viewset",movies_viewset,basename="user_viewset")
routers.register("genres_viewset", genres_viewset, basename="genres_viewset")
routers.register("directors_viewset", directors_viewset, basename="directors_viewset")
routers.register("certified_viewset", certified_viewset, basename="certified_viewset")
routers.register("actors_viewset", actors_viewset, basename="actors_viewset")


urlpatterns = routers.urls
urlpatterns += [
    path("signup/",signup,name="signup"),
    path("login/",login,name = "login"),
    path('home',home, name = 'home'),
    path('profiles',profiles, name = 'profiles'),
]