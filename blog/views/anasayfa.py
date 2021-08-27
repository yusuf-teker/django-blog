from django.shortcuts import render
#Yazılarımızı anasayfa içinde göstermek için YazilarModeli ipmort edicem
from blog.models import YazilarModel    
from django.core.paginator import Paginator
from django.db.models import Q #Yada kullanmak için |


def anasayfa(request):
    yazilar = YazilarModel.objects.all()
        #datamızı çektik şimdi anasayfa.html'i düzenlicez

    # sayfanın üstündeki sayfa numarasına göre sayfa değiştirme
    sayfa = request.GET.get('sayfa') #www.blog/iletisim?sayfa=4 -> ise 4 değerini alır
    
    # girilen sorguya göre Böyle bir yazi varmı yok mu onu kontrol edicez
    sorgu = request.GET.get('sorgu') 
    if sorgu:
        yazilar = yazilar.filter(
            Q(baslik__icontains = sorgu) | #icerik veya baslik kisminde sorgudaki deger var ise tum bu yazilari getirir 
            Q(icerik__icontains = sorgu)    #birden fazla varsa 1 tanesini almak icin .distinct() fonksiyonunu cagırdık
        ).distinct()                        



   #paginator ile her sayfada 2 tane yazı kartı gosterilmesi için
    paginator = Paginator(yazilar,2)

    context = {
        'yazilar': paginator.get_page(sayfa) #yazilar tum cardları getirirdi, paginator tum kartları sayfalara ayırdı 2şer 2şer
            #biz kaçıncı sayfayı girersek o sayfadaki 2 kartı döndürecek
    }
    return render(request, 'pages/anasayfa.html', context = context)
        #render fonksiyonu applerin icidne direkt templates klasörüne bakar o yüzden onu yazmadan onun altındaki blog/.. kısmını yazdık
        #context sözlügü olsuturup icindeki bilgileri rendera gönderirsek html kodları icinde {{isim}} şeklinde bu degerleri kullanabiliriz