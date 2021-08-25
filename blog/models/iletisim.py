from django.db import models

class IletisimModel(models.Model):
    email = models.EmailField(max_length=200)
        #email olup olmadıgnıı kontrol eder
    isim_soyisim = models.CharField(max_length=150)
    mesaj = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'iletisim'
        verbose_name = "İletisim"
        verbose_name_plural = "İletisim"


    def __str__(self):
        return self.email