from django.contrib import admin

#Admin Modelini Kalıtım Yoluyla alıyoruz
from django.contrib.auth.admin import UserAdmin

from account.models import CustomUserModel

class CustomAdmin(UserAdmin): #UserAdmin'e gidip bakabiliriz oda admin.ModelAdmin'i parametre olarak alıyor
    #model'ı override ediyoruz
    model = CustomUserModel
    list_display = ('username', 'email')
    #Avatarı eklemek için UserAdmin icindeki fieldSetlerle beraber kendi fieldımızıda ekliyeceğiz  
    # yani fielseti override ediyoruz ama eskilerinide alıyoruz
    fieldsets = UserAdmin.fieldsets + (
        ('Avatar Değiştirme Alanı', {
            'fields': ['avatar']
        }),)
    

admin.site.register(CustomUserModel, CustomAdmin)