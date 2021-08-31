from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
    #otomatik şifre değiştir formu
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required(login_url='/')
def sifre_degistir(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            kullanici = form.save() #bir formdan (yeni sifresini vs irdigi geliyorsa bilgileri al ve kullaniciyi olustur)
            update_session_auth_hash(request,kullanici) #şifre değişince kullanıcıyı atmak yerine oturumunu güncellesn
            messages.success(request, 'Şifre başarıyla değiştirildi.')
            return redirect('sifre-degistir')

    else:
        form = PasswordChangeForm(request.user)
        
    return render(request, 'pages/sifre-degistir.html',context={
        'form': form
    } )