from django.shortcuts import render

from blog.models import YazilarModel    
from django.core.paginator import Paginator
from django.db.models import Q 


def anasayfa(request):
    yazilar = YazilarModel.objects.all()
     
    sayfa = request.GET.get('sayfa') 
    sorgu = request.GET.get('sorgu') 
    if sorgu:
        yazilar = yazilar.filter(
            Q(baslik__icontains = sorgu) | 
            Q(icerik__icontains = sorgu)   
        ).distinct()                        

    paginator = Paginator(yazilar,2)

    context = {
        'yazilar': paginator.get_page(sayfa) 
    }
    return render(request, 'pages/anasayfa.html', context = context)
