from account.models import CustomUserModel
from enum import auto
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from blog.models import YazilarModel 

from blog.abstract_models import DateAbstractModel

class YorumModel(DateAbstractModel):
    yazan = models.ForeignKey('account.CustomUserModel', on_delete=CASCADE,related_name='yorum')

    yazi = models.ForeignKey(YazilarModel, on_delete=CASCADE, related_name='yorumlar')
  
    yorum = models.TextField()

    class Meta:
        db_table =  'yorum' 
        verbose_name = 'Yorum' 
        verbose_name_plural = 'Yorumlar' 
    
    def __str__(self):
        return self.yazan.username

