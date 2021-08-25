from enum import unique
from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
    #Sekilli yazilar icim RichTextField


class YazilarModel(models.Model):
    baslik = models.CharField(max_length=50)
    icerik = RichTextField() #models.TextField() yerine RichTextField kullanarak tema olarak ayarlanabilir bir metin alanı yaptık
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
        #auto_now_add -> Yazilar tablomuzda bir kayıt olusturuldugunda olusturulma_tarihi otomatik olusutulup eklenecek
    duzenlenme_tarihi =  models.DateTimeField(auto_now=True)
        #Yazilar tablosundaki icerik her degistiginde duzenlenme tarih alanı degistirdigimiz tarih olacak
    slug = AutoSlugField(populate_from = 'baslik', unique = True)
        #slugı baslik degiskeninden otomatik olustur    
    kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi')
        #Bir yazi birden cok kategoride olabilir o yüzden ManyToManyField
    resim = models.ImageField(upload_to = 'yazi_resimleri')
        #resimler yazi_resimleri  adında biyerde tutulacka
    yazar = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="yazilar")
        #Bir yazardan birden cok yaziya ulasabiliriz
        #on_delete=models.CASCADE, Egerki yazar silinirse onunla ilgili tüm yazilar silinir

    class Meta:
        verbose_name = 'Yazi'
        verbose_name_plural = 'Yazilar'
        db_table = 'Yazi'
            #Yazi adinda bir db tableında bilgiler tutulsun
    
    def __str__(self) :
        return self.baslik
    


         