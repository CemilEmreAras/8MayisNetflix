from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    isim=models.CharField(max_length=50, verbose_name="İsminizi Giriniz")
    resim=models.FileField(upload_to="profiles/",verbose_name="Profil Resmi")
    def __str__(self):
        return self.isim
    
class Kullanici(models.Model):
    isim=models.CharField(max_length=100)
    soyisim=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    resim=models.FileField(upload_to="kullanicilar/")
    tel=models.IntegerField()
    dogum=models.DateField()
    oluşturulma_tarih=models.DateField(auto_now_add=True,editable=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.isim
