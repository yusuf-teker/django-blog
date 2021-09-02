from django.contrib import admin
from blog.models import KategoriModel,YazilarModel,YorumModel,IletisimModel
# Register your models here.
admin.site.register(KategoriModel)


@admin.register(YazilarModel)                        
class YazilarAdmin(admin.ModelAdmin):
    list_display=('baslik','olusturulma_tarihi','duzenlenme_tarihi')
    search_fields = ('baslik','icerik')

@admin.register(YorumModel)    
class YorumAdmin(admin.ModelAdmin):
    list_display= ('yazan','olusturulma_tarihi', 'duzenlenme_tarihi')
    search_fields = ('yazan__username',)

@admin.register(IletisimModel)   
class IletisimAdmin(admin.ModelAdmin):
    list_display= ('isim_soyisim','olusturulma_tarihi'  )
    search_fields = ('email',)
