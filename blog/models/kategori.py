from django.db import models
from autoslug import AutoSlugField

class KategoriModel(models.Model):
    isim = models.CharField(max_length=30, blank= False, null=False)
    #otomatik artan id ekleniyor models.Model icinde    
    slug = AutoSlugField(populate_from='isim', unique= True)
    #unique = true sayesinde aynı adda 2. bir slag olustugunda ornegin
    #yusufteker/kategori/django-egitimi varsa 2. kez django-egitimi slugı olsuturuldugunda yusufteker/kategori/django-egitimi2 olacak

    class Meta:
        db_table = 'kategori'
        #Soldaki Kategori Models tiklayinca kategorilerin girildiği yerin ismini degistirmek
        verbose_name_plural= 'Kategoriler' #kategori models yerine kategoriler yazıcak

        #Kategori listesinin en üstündeki Baslık Select kategori models to change olarak
        verbose_name = "kategori" 

    #Admin panelinde objenin türü/adı yazıyor
    #Ordaki ismin düzgün gözükmesi icin classın isim degiskenini objenin türü/ismi yapıyoruz  
    #KARGEORI MODEL altındaki listedeki elemanların ismi    
    def __str__(self):
        return self.isim

    
