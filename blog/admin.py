from django.contrib import admin
from blog.models import KategoriModel,YazilarModel,YorumModel,IletisimModel
# Register your models here.
admin.site.register(KategoriModel)


@admin.register(YazilarModel)                                #admin paneliyle iliskilendirme        
class YazilarAdmin(admin.ModelAdmin):
    list_display=('baslik','olusturulma_tarihi','duzenlenme_tarihi')
        #admin deki yazilar kisminde yaziların baslik ve tarihlerde gozukecek
    search_fields = ('baslik','icerik')
        #Yazilar kısmında arama yapmaya imkan verir baslik ve icerik olarak arama yapılabilir
   
@admin.register(YorumModel)    
class YorumAdmin(admin.ModelAdmin):
    list_display= ('yazan','olusturulma_tarihi', 'duzenlenme_tarihi')
    search_fields = ('yazan__username',)
        #yorum modleinde yazan degiskenini User ile iliskilendirmistik -> User'da databasede auth_user'ı temsil ediyor gibi birşey
        #sqlite tablosunde aut_user'a baglı -> auth_user tablsounun icindeki username'a gore arama yapıcaz -> __username

@admin.register(IletisimModel)   
class IletisimAdmin(admin.ModelAdmin):
    list_display= ('isim_soyisim','olusturulma_tarihi'  )
    search_fields = ('email',)
        #yorum modleinde yazan degiskenini User ile iliskilendirmistik -> User'da databasede auth_user'ı temsil ediyor gibi birşey
        #sqlite tablosunde aut_user'a baglı -> auth_user tablsounun icindeki username'a gore arama yapıcaz -> __username

