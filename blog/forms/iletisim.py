from django import forms
#from django.forms import fields
#Not1: İstersek boostraptan form alabilriz
from blog.models import IletisimModel
from django.core.mail import send_mail #Mail göndermek icin


class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimModel 
        fields = ('isim_soyisim' , 'email', 'mesaj') # İletisim modeli icinde hangi fieldları istiyoruz

    def send_email(self,mesaj):
        send_mail(
            subject='İletişim Formundan Yeni Mesaj Var!',
            message=mesaj,
            from_email=None, # None ise settignsdeki default maili kullanır
            recipient_list=['y.teker.1907.1907@gmail.com'],
            fail_silently=False
        )


###################################################################################
#bu formu views icindeki iletisim de kullanacam
#DJANGO FORMU
#class IletisimForm(forms.Form): #classın form olabililmesi icin forms.Form'dan türemeli
    # Gerekli field'ları alalım  
 #   email    = forms.EmailField(label = 'E Posta', max_length=100) #istersek label ekleyebilriz Email yerine E Posta yazacak
 #   isim_soyisim = forms.CharField(label = 'İsim Soyisim',max_length=40)
 #   mesaj = forms.CharField(widget=forms.Textarea())     #TextArea yapmak için ekstradan widget kullanmak gerekiyor
        #boostraptki formlar'da mesela class olarak form-control kullanmıs birini bizde bunu attr olarak ekleyip tasarımımı daha güzel yapabilriz

    #Widget Terimi: Field'lar otomatik olarak bir widget seçer.
    #https://docs.djangoproject.com/en/3.2/ref/forms/widgets/
        #bu widget bir html elementine eş değer ve biz istersek bu widgetların özelliklerini override edebilriz ornegin sınıfını degistirelim
        #bu sayede icine attrb ekleyebiliriz Ornegin -> widget=forms.Textarea(attrs = {
        # 'class' : 'yusuf'} ) -> artık mesajın sınıfı yusuf
        
####################################################################################

# YONTEM 2  FORM MODEL KULLANNIMI 

