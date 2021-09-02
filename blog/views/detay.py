from django.shortcuts import get_object_or_404, redirect, render
from blog.models import YazilarModel
from blog.forms import YorumEkleModelForm, yorum_ekle
from django.contrib import messages
from django.views import View 

import logging

logger = logging.getLogger('konu_okuma') 

class DetayView(View):

    http_method_names = ['post', 'get'] 
    yorum_ekle_form = YorumEkleModelForm 
    def get(self, request, slug):
        yazi = get_object_or_404(YazilarModel,slug = slug)
         
        if request.user.is_authenticated :
            logger.info( yazi.baslik+' okundu... '+request.user.username)

        yorumlar = yazi.yorumlar.all()
        return render(request, 'pages/detay.html', context = {
        'yazi': yazi,
        'yorumlar' : yorumlar,
        'yorum_ekle_form': self.yorum_ekle_form 
        })
    def post(self, request, slug):
        yazi = get_object_or_404(YazilarModel,slug = slug)
        yorum_ekle_form = self.yorum_ekle_form(data=request.POST)
        if yorum_ekle_form.is_valid():
            yorum = yorum_ekle_form.save(commit = False)
            yorum.yazan = request.user
            yorum.yazi = yazi 
            yorum.save(  )
            messages.success(request,"Yorum eklendi.")
        return redirect('detay',slug=slug)


