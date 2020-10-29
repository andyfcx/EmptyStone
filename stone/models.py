from django.db import models
from django.db.models import CharField, IntegerField, EmailField, URLField

# Create your models here.


class User(models.Model):
    name = CharField(max_length=50)
    email = EmailField(max_length=100)
    # _id = AutoField()
    priv = CharField(max_length=20, default='Moderator')
    tel = CharField(max_length=10, default=None)
    password  = CharField(max_length=100, default=None)




class GCSFile(models.Model):
    fileName = CharField(max_length=100)
    fileType = IntegerField()
    gcsBucket = CharField(max_length=100)
    gcsDir = CharField(max_length=100)
    size = IntegerField(help_text="enum of size")
    url = URLField()
    height = IntegerField()
    width = IntegerField()
    iptc = CharField(max_length=100)
