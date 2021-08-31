from django import forms
from django.forms import fields
from blog.models import YorumModel

class YorumEkleModelForm(forms.ModelForm):
    class Meta:
        model = YorumModel
        fields = ('yorum', )
            #Yorum model icinde yazar yazi ve yorum var bize sadece  yorum lazım
            
