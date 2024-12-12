from django.db import models

class Registered_list(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)

