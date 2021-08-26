from django.shortcuts import render

def anasayfa(request):
    context = {
        'isim' : 'Yusuf',
        'soyisim' : 'Teker'
    }
    return render(request, 'pages/anasayfa.html', context = context)
        #render fonksiyonu applerin icidne direkt templates klasörüne bakar o yüzden onu yazmadan onun altındaki blog/.. kısmını yazdık
        #context sözlügü olsuturup icindeki bilgileri rendera gönderirsek html kodları icinde {{isim}} şeklinde bu degerleri kullanabiliriz