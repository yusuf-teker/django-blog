
from django.contrib import admin
from django.urls import path,include
    #include sayesinde config dısındaki diğer applerde olusturulan urls.py dosyasındaki pathlerle bir nevi iletisim kurulacak
from blog.views import iletisim


from django.conf.urls.static import static
    #medya dosyalarını yayınlamamızı saglayan fonksiyon
from django.conf import settings
    #MEDIA_URL VE MEDIA_ROOT a ulaskmak icin




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls'))
        #Birisi /blog/ + (blog.urls icindeki birşey örnegin 'iletisim' kısmı yazarsa) path('ietisim', iletisim) -> iletisim fonksiyonunu çağırıyor
            #blog icindeki urls icindeki path icindeki iletisim fonksiyonunuda blog icindeki views icinde iletisim.py adındaki kolasörden import ediyoruz
        #include sayesinde blog.urls içindeki tüm pathleri girmiş gibi olduk
        
        #www.yusufteker/blog/ (iletisim veya  ileride baska urls ler olusturursak o geleck)
        #'blog/' yerine '' bos bırakırsak www.yusufteker/iletisim seklinde girilebilir
            # path('',include('blog.urls'))
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
        #1.parametrenin karsılığı /media/ yani /media/ kısmından sonraki kısım girilicek
        #2.parametre url'lerin kaynagı neerede
