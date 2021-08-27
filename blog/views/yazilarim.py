from django.core import paginator
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required #egerki login olmamıs birisi yazilarim sayfasına girmeye calısırsa hata yerine login kısmına yönlendirme

@login_required(login_url='/')#login kısmımızz yok diye anasayfaya yönlendirdik
def yazilarim(request):
    yazilar = request.user.yazilar.order_by('-id') #yazi.py icinde yazilar ile related iliskisi kurmustuk Bu sayede YazilarModel kullanamdan gerekli yazilari user üzerinden çekebiliriz
        #Giris yapan user'ın yazilarına ulastık
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar, 2)

    return render(request, 'pages/yazilarim.html', context= {
        'yazilar' : paginator.get_page(sayfa),
    })