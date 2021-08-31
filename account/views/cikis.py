from django.contrib.auth import logout
    #djangonun default logout fonksiyonunu kllanabilirz
from django.shortcuts import redirect


def cikis (request):
    logout(request) # cikis yapıldı
    return redirect('anasayfa')