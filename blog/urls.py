import django
from blog.views import YaziEkleCreateView
from blog.views.anasayfa import anasayfa
from django.urls import path
from blog.views import IletisimFormView,anasayfa,KategoriListView, YaziGuncelleUpdateView, YaziSilDeleteView,yazilarim,DetayView, YaziEkleCreateView, yorum_sil

from django.views.generic import TemplateView, RedirectView #TemplateView - RedirectView

urlpatterns = [
    path('', anasayfa, name='anasayfa'), #istersek 3. bir parametre ile url'e isim verebiliriz böylece html icinde kullanırken kolaylık olur
    
    
    #path('iletisim',iletisim, name='iletisim'),
    path('iletisim',IletisimFormView.as_view(), name='iletisim'),


    #path('kategori/<slug:kategoriSlug>',kategori, name='kategori'),
        #slug tipinde bir deger isitoruz adını KategoriSlug koyduk
            #8000/kategori/(slug tipinde deger)
            #Bu slug degeri kategori.py views'imiz icindeki kategori fonksiyonunu KategoriSlug parametresi olarak gönderilir
    path('kategori/<slug:kategoriSlug>',KategoriListView.as_view(), name='kategori'),
    
    
    path('yazilarim', yazilarim , name='yazilarim'), #/yazilarim , yazilarim fonksiyonu , htmlde yazilarim olarak kullan 
    path('yazi/<slug:slug>', DetayView.as_view(), name='detay'),

    #path('detay/<slug:slug>', detay, name='detay'),
    path('detay/<slug:slug>', DetayView.as_view(), name='detay'),



    #path('yazi-ekle', yazi_ekle, name = 'yazi-ekle') ,
    path('yazi-ekle', YaziEkleCreateView.as_view(), name = 'yazi-ekle') ,
        #1.par url'de girilcek yer .../yazi-ekle  
        #2.par view 'ımız
        #3.par html'de kullaacagımız kısım

    path('yazi-guncelle/<slug:slug>', YaziGuncelleUpdateView.as_view(), name = 'yazi-guncelle' ),
        #guncellenecek yazıyı slug olarak istiycez
    
    
    
    #DeleteViewKullanımı
    #path('yazi-sil/<slug:slug>', yazi_sil, name='yazi-sil'),
    path('yazi-sil/<slug:slug>',YaziSilDeleteView.as_view(), name='yazi-sil'),
   
   
    path('yorum-sil/<int:id>', yorum_sil, name = 'yorum-sil'),


    #TemplateView Kullanımı
    path('hakkinda', TemplateView.as_view(#templateViwe classbased view'dur ve bunu override etmek istersek as_view kullanabiliriz
        template_name = 'pages/hakkinda.html' #template_name'yi override edelim

    ), name='hakkimda'), 

    #RedirectView Kullanımı
    path('yonlendir',RedirectView.as_view(
        url = 'https://www.google.com'
    ), name='yonlendir'),

    path('email-gonderildi', TemplateView.as_view(
        template_name = 'pages/email-gonderildi.html'
    ),name='email-gonderildi')
] 
 