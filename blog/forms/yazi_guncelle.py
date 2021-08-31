from django import forms
from blog.models import YazilarModel
## YAZI EKLEME FORMU 

class YaziGuncelleFormModel(forms.ModelForm):
    class Meta:
        model = YazilarModel

        #Butun bu fieldları yazmak yerine almayacağımız fieldları yazabilriz
        #field = ('resim','baslik','icerik','kategoriler')
        exclude = ('slug','yazar') # bu ikisi haric hepsini al
        
