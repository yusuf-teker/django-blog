from django import forms
from django.shortcuts import redirect, render

from blog.forms import IletisimForm #FORMLAR Vıdeosunda

from blog.models import IletisimModel  # Formdan çektiğim veriyi IletisimModel -> Iletisim Databasemize ekliycez

def iletisim(request):
    form =  IletisimForm(data={ # İstersek default degerler verebiliriz
        'isim_soyisim' : 'Dilber Tekin',
        'email' : ''
    }) 

    #Iletisim.html'den form yardımıyla POST seklinde gonderdigimiz veriyi alalım
    if request.method == 'POST':
        #print(request.POST) #reques.POST geliyor ama içindeki verileri validate etmemiz gerekiyor çünkü html form'da  öğeyi denetle yapıp max lenght require gibi şeyleri kaldırabilir böylece boş bir form bile gönderebilirler
        #formdan aldıgımız verileri IletisimFormuna parametre olarak göndrebilriz
        form = IletisimForm(request.POST)
        #Formdan gelen bilgileri kontrol etmemiz lazım
        if form.is_valid(): #eğer valid ise dataları  ve databasemize ekleyebiliriz
            
            ###################################### 
            """#çektiğimiz verilrei DataBasemize ekleyebiliriz. bunu İcin öncelikle bir IletisimModel objesi olustucaz (databasemizde iletisim olarak geciyor)
            iletisim = IletisimModel()
            iletisim.email = form.cleaned_data.get('email')
            iletisim.isim_soyisim = form.cleaned_data.get('isim_soyisim')
            iletisim.mesaj = form.cleaned_data.get('mesaj')
            #ILetısımModel DATAMIZI DATABASEYE GONDERME
            iletisim.save() """
            ###########################################
            # 2.YOL -> Form Model'i kullanırsak form Model'de tüm fieldları (email isim vs ) verdigimiz icin
            form.save()#direkt olarak form.save() diyebiliriz



            #Yonlendirme -> verimizi kaydettikten sonra anasayfa.htmle'e yonlendiriyoruz
            return redirect('anasayfa')
            
            



    context = { 
        'form': form #Formu iletisim sayfaınsa gönderelim   
    }
    return render(request, 'pages/iletisim.html', context = context)
        #render fonksiyonu applerin icidne direkt templates klasörüne bakar o yüzden onu yazmadan onun altındaki blog/.. kısmını yazdık
        #context sözlügü olsuturup icindeki bilgileri rendera gönderirsek html kodları icinde {{isim}} şeklinde bu degerleri kullanabiliriz