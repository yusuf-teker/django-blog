from django.shortcuts import render

def iletisim(request):
    context = {
        'isim' : 'Yusuf',
        'soyisim' : 'Teker'
    }
    return render(request, 'pages/iletisim.html', context)
        #render fonksiyonu applerin icidne direkt templates klasörüne bakar o yüzden onu yazmadan onun altındaki blog/.. kısmını yazdık
        #context sözlügü olsuturup icindeki bilgileri rendera gönderirsek html kodları icinde {{isim}} şeklinde bu degerleri kullanabiliriz