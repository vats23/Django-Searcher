from django.urls import include,path
from . import views

app_name="searcher"

urlpatterns = [
    path("",views.home,name="home"),
    path("register/",views.register,name="register"),
    path("finder/",views.finder,name="finder")
]
