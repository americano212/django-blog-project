from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Account(AbstractUser):
    name = models.CharField(max_length=5)
    nickname = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=11)

    birth_y = models.CharField(max_length=4,default='0')
    birth_m = models.CharField(max_length=2,default='0')
    birth_d = models.CharField(max_length=2,default='0')
    id_boj = models.CharField(max_length=20,default='-')
    id_cf = models.CharField(max_length=20,default='-')
    id_github = models.CharField(max_length=20,default='-')
    
    user_level = models.IntegerField(default=0)
    user_exp = models.IntegerField(default=0)
