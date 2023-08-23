from django.shortcuts import render,redirect
from .models import *
from user.models import * 
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, 'index.html')

def browseindex(request):
    filmler=Movie.objects.all()
    user =Profile.objects.all()
    context={
        "filmler":filmler,
        "user":user
    }
    return render(request, 'browse-index.html',context)

def olustur(request):
    if request.method == 'POST':
        isim=request.POST["isim"]
        resim=request.FILES["resim"]
       
        
        movie=Movie.objects.create(
            isim=isim,resim=resim
        )
        movie.save()
        messages.success(request,"film oluşturuldu")
        return redirect("browse-index")
    return render(request,"olustur.html")



def mailat(request):
    konu="Alışveriş"
    mesaj="bu ürünü almak istiyorum"
    from_email = 'neos.cemilemre@gmail.com'
    giden=['candinler4@gmail.com']
    send_mail(konu,mesaj,from_email,giden)
    return render(request,"posta.html")
