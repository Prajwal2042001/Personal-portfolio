from django.db import models

class Project_list(models.Model):
    title=models.CharField(max_length=500)
    abstract=models.CharField(max_length=10000)
    skills=models.CharField(max_length=500)
    slno=models.IntegerField()
    pphoto=models.ImageField(upload_to='poster')
