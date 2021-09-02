from django import forms
from django.shortcuts import redirect, render

from blog.forms import IletisimForm
from blog.models import IletisimModel 

from django.views.generic import FormView
from django.core.mail import send_mail

class IletisimFormView(FormView):
    template_name = 'pages/iletisim.html'
    form_class = IletisimForm
    success_url = '/email-gonderildi'
    def form_valid(self,form):
        form.save()
        form.send_email(mesaj= form.cleaned_data.get('mesaj'))
        return redirect(self.success_url)


