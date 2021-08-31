from django.contrib.auth.decorators import login_required
from django.http import request
from blog.models import YazilarModel
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy #bu sayede success_url kullanım redirect yapıcaz
from django.contrib.auth.mixins import LoginRequiredMixin   

class YaziSilDeleteView(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('giris')
    template_name = 'pages/yazi_sil_onay.html' #yeni olusturcaz
    success_url = reverse_lazy('yazilarim')
    def get_queryset(self):
        #geriye query set döndürmemiz gerekiyor get_object tek bir obje döndürdüğü için bunu yerine 
        #yazi = get_object_or_404(YazilarModel, slug = self.kwargs['slug'], yazar = self.request.user)
        yazi = YazilarModel.objects.filter(slug = self.kwargs['slug'], yazar = self.request.user) #kullanabilirim
            #yazilar içinde linkteki slugın slugı ile eşleşen yazıyı bul. İstek yapak kullanıcı bu yazının sahibimi kontrol et. sorun yoksa yaziyi gönder
        return yazi


@login_required(login_url= '/')
def yazi_sil(request, slug): # slug belli bir yaziyi silcez o yüzden
    #yazilar modelinden bakıcaz giriş yapan kişi ile yazi sahibi uyusuyormu
    get_object_or_404(YazilarModel, slug = slug, yazar = request.user).delete()
        #1.par database
        #2.par girilen slug yazilar modeli icinde var mı
        #3.par aktif kullanıcı bu slug daki yazının sahibi mi
        # .delete() 2 ve 3 sağlanırsa  YazilarModelindeki bu datayı (objeyi) sil
    return redirect('yazilarim') #slme bitince yazilarım kısmına gönder
    


  