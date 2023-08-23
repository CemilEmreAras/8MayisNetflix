from django.urls import path,include
from .views import *

urlpatterns = [
   
    path('register/', UserRegister,name="register"),
    path('login/', UserLogin,name="login"),
    path('logout/', UserLogout,name="logout"),
    path('profiles/', profiles,name="profil"),
    path('create/', createProfile,name="create"),
    path('hesap/', hesap ,name="hesap"),
    path('delete/', userDelete,name="delete"),
    
]