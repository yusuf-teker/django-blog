from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.forms import ProfilGuncelleForm

@login_required(login_url='/')
def profil_guncelle(request):
    if request.method == 'POST':
        form = ProfilGuncelleForm(request.POST,request.FILES,instance = request.user)
        if form.is_valid():
            messages.success(request,'Profil başarıyla güncellendi.')
    else:
        form = ProfilGuncelleForm(instance = request.user)
    return render(request, 'pages/profil-guncelle.html',context={
        'form': form
    })