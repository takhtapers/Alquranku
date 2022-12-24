from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    
    def __str__(self):
         return self.nama
    
    class meta :
        verbose_name_plural = "Kategori"

class Artikel(models.Model):
    nama = models.CharField(max_length=100,blank=True,null=True)
    judul = models.CharField(max_length=100)
    body = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)
    
    class meta :
        ordering = ['-id']
        verbose_name_plural = "Artikel"
        
class Alquran(models.Model):
    arti = models.CharField(max_length=1000)
    asma = models.CharField(max_length=1000)
    audio = models.FileField()
    ayat = models.IntegerField()
    keterangan = models.TextField()
    nama = models.CharField(max_length=1000)
    nomor = models.IntegerField()
    rukuk = models.IntegerField()
    type = models.CharField(max_length=100,blank=True,null=True)
    urut = models.IntegerField()
    
    def __str__(self):
        return "{} - {}".format(self.nama, self.arti)

class Doa(models.Model):
    id = models.IntegerField(primary_key=True)
    doa = models.CharField(max_length=100)
    ayat  = models.CharField(max_length=1000)
    latin = models.TextField()
    artinya = models.TextField()
    
    def __str__(self):
        return "{} - {}".format(self.id, self.doa)

    
    
    
    

