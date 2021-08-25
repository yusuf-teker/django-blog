from django.db import models

# Hazırda bulunan auth_user'dan kalıtım alıp custom user olusturmak istiyorum
from django.contrib.auth.models import AbstractUser
    #ctrl ile AbstractUser icine gir
class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to = 'avatar/',blank = True,null = True)
        #Blank true resim yüklemek istemez ise
    class Meta:
        db_table = 'user'
        verbose_name = "Kullanıcı"
        verbose_name_plural = "Kullanıcılar"
    def __str__(self):
        return self.username
            #Zateen kalıtımla çopu user degiskenlerini iceriyor username de onlardan biri

#Degault auth_user yerine bunu kullanmak icin settings e gidip AUT_USER_MODEL="account.CustomUserModel"
#Artık daha önce User ile iliskilendirdigimiz yazi ve yorum modellerini degistirmemiz lazım

