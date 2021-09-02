import django
from blog.views import YaziEkleCreateView
from blog.views.anasayfa import anasayfa
from django.urls import path
from blog.views import IletisimFormView,anasayfa,KategoriListView, YaziGuncelleUpdateView, YaziSilDeleteView,yazilarim,DetayView, YaziEkleCreateView, yorum_sil

from django.views.generic import TemplateView, RedirectView 

urlpatterns = [
    path('', anasayfa, name='anasayfa'), 
    path('iletisim',IletisimFormView.as_view(), name='iletisim'),
    path('kategori/<slug:kategoriSlug>',KategoriListView.as_view(), name='kategori'),
    path('yazilarim', yazilarim , name='yazilarim'),
    path('yazi/<slug:slug>', DetayView.as_view(), name='detay'),
    path('detay/<slug:slug>', DetayView.as_view(), name='detay'),
    path('yazi-ekle', YaziEkleCreateView.as_view(), name = 'yazi-ekle') ,
    path('yazi-guncelle/<slug:slug>', YaziGuncelleUpdateView.as_view(), name='yazi-guncelle'),
    path('yazi-sil/<slug:slug>',YaziSilDeleteView.as_view(), name='yazi-sil'),
    path('yorum-sil/<int:id>', yorum_sil, name = 'yorum-sil'),
    path('hakkinda', TemplateView.as_view(
        template_name = 'pages/hakkinda.html' 

    ), name='hakkinda'), 
    path('yonlendir',RedirectView.as_view(
        url = 'https://www.google.com'
    ), name='yonlendir'),
    path('email-gonderildi', TemplateView.as_view(
        template_name = 'pages/email-gonderildi.html'
    ),name='email-gonderildi')
] 
 