from django import template
from blog.models import KategoriModel, kategori

register = template.Library() #temlpate tagını ve filterlarını kayıt etmek icin

#kendi tagimizi olusturalım
@register.simple_tag
def kategori_list( ):
    kategoriler = KategoriModel.objects.all()
    return kategoriler
