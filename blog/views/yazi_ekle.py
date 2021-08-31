from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.urls.base import reverse,reverse_lazy
from blog.forms import YaziEkleModelForm
from django.views.generic import CreateView
from blog.models import YazilarModel

from django.contrib.auth.mixins import LoginRequiredMixin
    #LoginReuqiredView  classa par olarak ekle ve login_url override et

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
        return super().form_valid(form) #eğer valid'se succec urli çalıştırılır

    #kayıt işlemi yapıldıktan sonra ne yapalım
    #Valid işlemi yapıldıktan sonra OTOMATİK olarak çağrılır
    def get_success_url(self): 
        return reverse('detay', kwargs={
            'slug': self.object.slug
        })


""" 
@login_required(login_url='/') #login yapılmamızsa anasayfaya yonlendir
def yazi_ekle(request):
    form = YaziEkleModelForm(request.POST or None, files = request.FILES or None) #if'lerle ugrasmadan POST ise al yoksa None
        #data gelince files'in icine koy data gelmezse files = None
    if form.is_valid():
        yazi = form.save(commit = False)    #commit fale veriyi hazırla ama commit etme
        # cünkü bazi bilgilerimiz şuan eksik örnegin yazinin yazari kim vs bunları alıp sonra tekrar save edicez
        yazi.yazar = request.user
        yazi.save()

        form.save_m2m() #  many to many kullanmıstık yazilarda kategorilerle iliskili olarak 
            #Bu yaziyi ekledigimizde kategoriler db'inede gitsin diye bu kodu ekliyor gibi bişeyiz
 
        return redirect('detay', slug = yazi.slug) # yeni olusturulan yazinin detay sayfasına yonlendirme yapıyoruz
            #bu detay sayfası slug istiyordu yazi'nin slugını verdik

    return render(request, 'pages/yazi-ekle.html', context={
        'form' : form 
    }) """