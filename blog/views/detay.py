from django.shortcuts import get_object_or_404, render
from blog.models import YazilarModel

def detay(request, slug): 
    #yusufteker/yazi/deneme3 (deneme 3 burada slug)
    yazi = get_object_or_404(YazilarModel,slug = slug) #detaySlug Bir Databasede bir yazi ile uyusuyormu kontrol
    yorumlar = yazi.yorumlar.all() #Ters iliski sayesinde Yorumları import etmeden elimizdeki yazi(lar)'in yorumlarını çekiyoruz
    return render(request, 'pages/detay.html', context = {
        'yazi': yazi,
        'yorumlar' : yorumlar

    })
