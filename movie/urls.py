from django.urls import path
from .views import *


urlpatterns = [
    path("", browseindex,name="browse-index"),
    path("olustur/", olustur,name="olustur"),
    
]
