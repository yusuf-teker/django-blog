from django.contrib import admin
from blog.models import KategoriModel,YazilarModel
# Register your models here.
admin.site.register(KategoriModel)



class YazilarAdmin(admin.ModelAdmin):

    list_display=('baslik','olusturulma_tarihi','duzenlenme_tarihi')
        #admin deki yazilar kisminde yaziların baslik ve tarihlerde gozukecek

    search_fields = ('baslik','icerik')
        #Yazilar kısmında arama yapmaya imkan verir baslik ve icerik olarak arama yapılabilir
    
   
       

admin.site.register(YazilarModel,YazilarAdmin)