from django.shortcuts import get_object_or_404, redirect, render
from blog.models import YazilarModel
from blog.forms import YorumEkleModelForm, yorum_ekle
from django.contrib import messages
from django.views import View #Viewlarımızı class-based sınıf yapma


class DetayView(View):

    http_method_names = ['post', 'get'] # bu view'a post ve get islemleri yapılabilsin diyoruz. OPTIONAL
    yorum_ekle_form = YorumEkleModelForm #Bunu yukarı aldım hem postta hem gette kullanacağım için

    #GET icin ayrı 
    def get(self, request, slug):
        yazi = get_object_or_404(YazilarModel,slug = slug)
        yorumlar = yazi.yorumlar.all()
        return render(request, 'pages/detay.html', context = {
        'yazi': yazi,
        'yorumlar' : yorumlar,
        'yorum_ekle_form': self.yorum_ekle_form #self koymalıyız
        })
    #POST icin ayrı 
    def post(self, request, slug):
        yazi = get_object_or_404(YazilarModel,slug = slug)
        yorum_ekle_form = self.yorum_ekle_form(data=request.POST)
        if yorum_ekle_form.is_valid():
            yorum = yorum_ekle_form.save(commit = False)
            yorum.yazan = request.user
            yorum.yazi = yazi #yorum yazisi degil yorum yapılan icerigin yazısı
            yorum.save(  )
            messages.success(request,"Yorum eklendi.")
        return redirect('detay',slug=slug)



""" def detay(request, slug): 
    #yusufteker/yazi/deneme3 (deneme 3 burada slug)
    yazi = get_object_or_404(YazilarModel,slug = slug) #detaySlug Bir Databasede bir yazi ile uyusuyormu kontrol
    yorumlar = yazi.yorumlar.all() #Ters iliski sayesinde Yorumları import etmeden elimizdeki yazi(lar)'in yorumlarını çekiyoruz

    #yorum ekleme kısmı
    yorum_ekle_form = YorumEkleModelForm()
    if request.method == 'POST':
        yorum_ekle_form = YorumEkleModelForm(data=request.POST)
        if yorum_ekle_form.is_valid():
            yorum = yorum_ekle_form.save(commit = False)
            yorum.yazan = request.user
            yorum.yazi = yazi #yorum yazisi degil yorum yapılan icerigin yazısı
            yorum.save(  )
            
    #if ile yorum gonderimi yapıldıktan sonra yorum kısmı temizlensin diye ekledik
    yorum_ekle_form = YorumEkleModelForm()


    return render(request, 'pages/detay.html', context = {
        'yazi': yazi,
        'yorumlar' : yorumlar,
        'yorum_ekle_form': yorum_ekle_form #yorum ekle

    })
 """