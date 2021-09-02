from django import forms
#from django.forms import fields
#Not1: İstersek boostraptan form alabilriz
from blog.models import IletisimModel
from django.core.mail import send_mail #Mail göndermek icin


class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimModel 
        fields = ('isim_soyisim' , 'email', 'mesaj') 

    def send_email(self,mesaj):
        send_mail(
            subject='İletişim Formundan Yeni Mesaj Var!',
            message=mesaj,
            from_email=None,
            recipient_list=['y.teker.1907.1907@gmail.com'],
            fail_silently=False
        )

