from django.db import models

class Personal(models.Model):
    user_idx = models.AutoField(primary_key =True)
    user_id = models.CharField(max_length=13)
    user_pwd = models.CharField(max_length=64)
