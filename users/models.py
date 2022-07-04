from django.db import models

from cores.models import TimeStampModel

class User(TimeStampModel):
    kakao_id = models.BigIntegerField()
    name     = models.CharField(max_length = 100)
    email    = models.CharField(max_length = 200)
    password = models.CharField(max_length = 300)
    
    class Meta:
        db_table = 'users'