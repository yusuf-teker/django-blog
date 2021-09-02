from django import template
from blog.models import KategoriModel, kategori

register = template.Library()

@register.simple_tag
def kategori_list( ):
    kategoriler = KategoriModel.objects.all()
    return kategoriler
