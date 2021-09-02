from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel, KategoriModel
from django.core.paginator import Paginator
#kategori.py olusturduktan sonra views'deki inite koymayı unutma
#sonrasında views'deki urlpatterne ekleme yap
#urls'de slug tipinde KategoriSlug degiskeni istedik bunu kategori fonksiyonumnuza parametre olarak göndericez
#navbar'dan da kategorilere erismek icin url ayarlıcaz



from django.views.generic import ListView 

class KategoriListView(ListView):
  
    template_name = 'pages/kategori.html'
    context_object_name = 'yazilar'
    paginate_by = 2
    def get_queryset(self):
        
        kategori = get_object_or_404(KategoriModel, slug=self.kwargs['kategoriSlug']) 
        return kategori.yazi.all().order_by('-olusturulma_tarihi')

def kategori(request,kategoriSlug):

    kategori = get_object_or_404(KategoriModel, slug = kategoriSlug)

    yazilar = kategori.yazi.order_by('id')
    sayfa = request.GET.get('sayfa') 
    paginator = Paginator(yazilar, 2)
    context = {
        'yazilar': paginator.get_page(sayfa) ,
        'kategori_isim': kategori.isim
    }
    return render(request, 'pages/kategori.html', context = context)
 