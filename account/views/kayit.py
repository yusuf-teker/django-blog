from django.shortcuts import redirect, render
from django.contrib import messages
from account.forms import KayitFormu
from django.contrib.auth import login, authenticate


def kayit(request):
    if request.method == 'POST':
        form = KayitFormu(request.POST,)
        if form.is_valid():
            form.save() #Kayit işlemi tamamlandı.

            #Kayit oldutan sonra kullanıcı direkt olarak sayfaya girdirelim
                #once bilgilerini alalım
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            #dogrulama yaptıktan sonra
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('anasayfa')

    else:
        form = KayitFormu()
        
    return render(request, 'pages/kayit.html',context={
        'form': form
    })