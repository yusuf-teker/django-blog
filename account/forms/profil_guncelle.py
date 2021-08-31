from django.contrib.auth.forms import UserChangeForm
from account.models import CustomUserModel

#direkt UserChangeForm Kullanmaktansa bazı kısımları değiştirmek icin override edicez
class ProfilGuncelleForm(UserChangeForm):


    password = None #sifre degistiremesin
    class Meta:
        model=CustomUserModel
        #degistirmek istedigim alanla
        fields = ('email','first_name','last_name', 'avatar')