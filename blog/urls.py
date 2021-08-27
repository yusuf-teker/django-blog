from blog.views.anasayfa import anasayfa
from django.urls import path
from blog.views import iletisim,anasayfa,kategori,yazilarim

urlpatterns = [
    path('', anasayfa, name='anasayfa'), #istersek 3. bir parametre ile url'e isim verebiliriz böylece html icinde kullanırken kolaylık olur
    path('iletisim',iletisim, name='iletisim'),
    path('kategori/<slug:kategoriSlug>',kategori, name='kategori'),
        #slug tipinde bir deger isitoruz adını KategoriSlug koyduk
            #8000/kategori/(slug tipinde deger)
            #Bu slug degeri kategori.py views'imiz icindeki kategori fonksiyonunu KategoriSlug parametresi olarak gönderilir
    path('yazilarim', yazilarim , name='yazilarim') #/yazilarim , yazilarim fonksiyonu , htmlde yazilarim olarak kullan 
]
 