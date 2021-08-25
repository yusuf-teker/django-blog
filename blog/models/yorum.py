from account.models import CustomUserModel
from enum import auto
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from blog.models import YazilarModel #->Yazi modelimiz



class YorumModel(models.Model):
    #Her yorum bir yazarla iliskili o iliskiyi kuralım -> User üzerinden yorumu yazana erisebilmek icin
    yazan = models.ForeignKey('account.CustomUserModel', on_delete=CASCADE,related_name='yorum')
        #Yazar silinirse yorumda silinir
        #yazanin yorumlarına ulaskmak icin related_name yorum

    #Her yorum bir yaziya yapiliyor -> yazi silinirse yorumda silinmeli CASCADE
    yazi = models.ForeignKey(YazilarModel, on_delete=CASCADE, related_name='yorumlar')
        #yazinin yorumlarına erismek icin ters iliski kurup related_name yorumlar diyoruz

    #Yorum icinde TextField olusturuyoruz
    yorum = models.TextField()

    olusturulma_tarihi = models.DateTimeField(auto_now_add=True) #Olusturuldugu tarihi al
    duzenlenme_tarihi = models.DateTimeField(auto_now=True) #Her güncellendiğinde tekrar tarihi al 

    class Meta:
        db_table =  'yorum' #yorum adında bir tablo
        verbose_name = 'Yorum' #admin panelinde güzel görüntü icin
        verbose_name_plural = 'Yorumlar' #cohul gecen yerlerde yorum yerine yorumlar cıkıyor
    
    def __str__(self):
        return self.yazan.username

