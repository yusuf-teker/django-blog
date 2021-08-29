from django.shortcuts import render,redirect
from blog.forms import YaziEkleModelForm

def yazi_ekle(request):
    form = YaziEkleModelForm(request.POST or None, files = request.FILES or None) #if'lerle ugrasmadan POST ise al yoksa None
        #data gelince files'in icine koy data gelmezse files = None
    if form.is_valid():
        yazi = form.save(commit = False)    #commit fale veriyi hazırla ama commit etme
        # cünkü bazi bilgilerimiz şuan eksik örnegin yazinin yazari kim vs bunları alıp sonra tekrar save edicez
        yazi.yazar = request.user
        yazi.save()
        

        form.save_m2m() #  many to many kullanmıstık yazilarda kategorilerle iliskili olarak 
            #Bu yaziyi ekledigimizde kategoriler db'inede gitsin diye bu kodu ekliyor gibi bişeyiz
 
        return redirect('detay', slug = yazi.slug) # yeni olusturulan yazinin detay sayfasına yonlendirme yapıyoruz
            #bu detay sayfası slug istiyordu yazi'nin slugını verdik


    return render(request, 'pages/yazi-ekle.html', context={
        'form' : form 
    })