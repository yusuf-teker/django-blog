from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,redirect
from django.urls.base import reverse, reverse_lazy
from blog import forms
from blog.forms import YaziEkleModelForm
from blog.models import YazilarModel
from blog.forms import YaziGuncelleFormModel

from django.views.generic import UpdateView
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

class YaziGuncelleUpdateView(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('giris') #giris yapılmamışsa giriş sayfasına yönlendir
    template_name = 'pages/yazi-guncelle.html'
    fileds = ('baslik','icerik','resim','kategoriler') #guncellenecek alanlar 
    #Bu sefer get_queryset yerine get object kullanalım ikiside iş görür
    def get_object(self):
        yazi = get_object_or_404(
            YazilarModel,
            slug = self.kwargs.get('slug'), #link kısmından gelen slug'a esit olanı bul
            yazar = self.request.user
        )
        return yazi #tek bir obje döndrüyüor ama bizden query set istiyor bu yüzden fields'lari eklicez
    def get_success_url(self):
        return reverse('detay',kwargs={
            'slug': self.get_object().slug
        })

@login_required(login_url='/') 
def yazi_guncelle(request, slug):
   
    yazi = get_object_or_404(YazilarModel, slug = slug, yazar = request.user )
        #girilen slug'da bir yazi varsa ve giris yapan kisinin yazarı ile uyusuyorsa formu olustur
    form = YaziGuncelleFormModel(request.POST or None, files= request.FILES or None, instance = yazi)
        #instance: initial gibi buldumuz yazinin icerigini form'un icine koyuyor. ufak bi degisiklik icin tüm yaziyi tekrardan yazmasın diye
    if form.is_valid():
        form.save()
        return redirect('detay', slug = yazi.slug) 
            #eger gücnellendiyse yazinin slug'ındaki yazinin detayına git

    #eger validate olmazsa esi formu geri gönder
    return render(request, 'pages/yazi-guncelle.html', context={
        'form' : form 
    })