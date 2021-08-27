from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel, KategoriModel
from django.core.paginator import Paginator
#kategori.py olusturduktan sonra views'deki inite koymayı unutma
#sonrasında views'deki urlpatterne ekleme yap
#urls'de slug tipinde KategoriSlug degiskeni istedik bunu kategori fonksiyonumnuza parametre olarak göndericez
#navbar'dan da kategorilere erismek icin url ayarlıcaz
def kategori(request,kategoriSlug):
    #8000/kategori/fasfasıf -> burada fasfasıf KategoriSlug degiskeni olur
    #get_object_or_404 fonksiyonunu import ettik bu sayede girilen slug gerçekten bir kategori adıyla uyusuyormu uyusmuyormu kontrol edecek
        #eger KategoriSlug gerçekten bir kategori adı ile uyusuyorsa açacak, uyusmuyorsa 404 hatası verecek
    kategori = get_object_or_404(KategoriModel, slug = kategoriSlug)
    #yazilar = YazilarModel.objects.all()
    #girilen kategorideki yazıları getirmeki için YazilarModel'de relatedname ile ters iliski kurmustuk
    yazilar = kategori.yazi.order_by('id')#order_by -id ile en son yazi en üstte olur       yazilar = kategori.yazi.all() # !!! 
    sayfa = request.GET.get('sayfa') 
    paginator = Paginator(yazilar, 2)
    context = {
        'yazilar': paginator.get_page(sayfa) ,
        'kategori_isim': kategori.isim
    }
    return render(request, 'pages/kategori.html', context = context)
