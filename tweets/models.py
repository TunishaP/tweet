from django.db import models
from django.db.models import deletion
from django.contrib.auth.models import User
from django import db
from cloudinary.models import CloudinaryField

# Create your models here.

class Tweet(models.Model):
    class Meta(object):
        db_table = 'tweet'

    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'Body', blank=True, null=True, max_length=148, db_index=True
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
    likes = models.PositiveBigIntegerField(
        'like', default=0, blank=True, db_index= True
    )
    image = CloudinaryField(
        'image', blank= True, db_index=True
    )
