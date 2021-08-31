from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUserModel


class KayitFormu(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ( #ilk 4ü bizim CustomerUserModelimizde var 
            'username',
            'email',
            'first_name',
            'last_name',
            'password1', #password1 ve 2 yi UserCreationForm sayesidne aldık
            'password2'
        )