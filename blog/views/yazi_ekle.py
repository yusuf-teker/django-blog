from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.urls.base import reverse,reverse_lazy
from blog.forms import YaziEkleModelForm
from django.views.generic import CreateView
from blog.models import YazilarModel

from django.contrib.auth.mixins import LoginRequiredMixin
   

class YaziEkleCreateView(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('giris ')
    template_name = 'pages/yazi-ekle.html'
    model = YazilarModel
    fields = ('baslik','icerik','resim','kategoriler')

    
    def form_valid(self, form):
        yazi = form.save(commit = False)  
        yazi.yazar = self.request.user
        yazi.save()
        form.save_m2m() 
        return super().form_valid(form) 


    def get_success_url(self): 
        return reverse('detay', kwargs={
            'slug': self.object.slug
        })

