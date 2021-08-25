from django.db import models

#Burdaki modelleri kullanacak olan modellerde Modele parametre olarak models.Model Yerin DateAbstractModel'i vericez zaten o models.Model'i kapsıyor

class DateAbstractModel(models.Model):
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True) #Olusturuldugu tarihi al
    duzenlenme_tarihi = models.DateTimeField(auto_now=True) #Her güncellendiğinde tekrar tarihi al 

    class Meta:
        abstract = True