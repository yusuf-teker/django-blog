from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import ProfilGuncelleForm

@login_required(login_url='/')
def profil_guncelle(request):
    if request.method == 'POST':
        form = ProfilGuncelleForm(request.POST,request.FILES,instance = request.user)
            #request.FILES dosya resim gibi şeyler icin
        if form.is_valid():
            messages.success(request,'Profil başarıyla güncellendi.')
    else:
        #Profil degistimek isteyenin bilgilerini profil güncelleme formunun icinde default olarak atıyoruz. Değiştirmesi kolay olsun diye
        form = ProfilGuncelleForm(instance = request.user)
            #basta Busayfaya geldiginde POST olmayacak else calısacak gerekli degisikliklerden sonra
                #bilgileri gönderdiginde bilgiler yine bu sayfa POST sayesinde alacak
                #ve bu sefer if kısmı calısacak gelen bilgilere gore degisim saglanacak
    return render(request, 'pages/profil-guncelle.html',context={
        'form': form
    })