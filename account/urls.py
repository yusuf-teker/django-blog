from account.views.profil import ProfilDetailView
from django.contrib import auth
from account.forms import kayit_formu
from django.urls import path
from account.views import cikis,kayit,profil_guncelle,sifre_degistir

from django.contrib.auth  import views as auth_views

urlpatterns = [
    path('giris', auth_views.LoginView.as_view(
        template_name = 'pages/giris.html'
    ), name= 'giris'), 
    path('cikis', cikis, name = 'cikis'),
    path('sifre-degistir', sifre_degistir, name= 'sifre-degistir'),
    path('profil-guncelle', profil_guncelle, name='profil-guncelle'),
    path('kayit',kayit, name = 'kayit'),
    path('kullanici/<str:username>', ProfilDetailView.as_view(), name='profil'),
]