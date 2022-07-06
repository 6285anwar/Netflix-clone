from django.db import models

# Create your models here.


class user_registration(models.Model):
    name = models.CharField(max_length=240, null=True)
    username = models.CharField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)

class movies(models.Model):
    username = models.ForeignKey(user_registration, on_delete=models.CASCADE,null=True,blank=True)
    moviename = models.CharField(max_length=240, null=True)
    movieurl= models.CharField(max_length=2400, null=True)
    movieposter = models.FileField(upload_to='images/', null=True, blank=True)

    