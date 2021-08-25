from django.contrib import admin
from blog.models import KategoriModel,YazilarModel,YorumModel
# Register your models here.
admin.site.register(KategoriModel)



class YazilarAdmin(admin.ModelAdmin):

    list_display=('baslik','olusturulma_tarihi','duzenlenme_tarihi')
        #admin deki yazilar kisminde yaziların baslik ve tarihlerde gozukecek

    search_fields = ('baslik','icerik')
        #Yazilar kısmında arama yapmaya imkan verir baslik ve icerik olarak arama yapılabilir

        

admin.site.register(YazilarModel,YazilarAdmin) #admin paneliyle iliskilendirme        
    
class YorumAdmin(admin.ModelAdmin):
    list_display= ('yazan','olusturulma_tarihi', 'duzenlenme_tarihi')
    search_fields = ('yazan__username',)
        #yorum modleinde yazan degiskenini User ile iliskilendirmistik -> User'da databasede auth_user'ı temsil ediyor gibi birşey
        #sqlite tablosunde aut_user'a baglı -> auth_user tablsounun icindeki username'a gore arama yapıcaz -> __username

admin.site.register(YorumModel,YorumAdmin)