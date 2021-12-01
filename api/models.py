from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Facebook(models.Model):
 user = models.CharField(max_length=100)
 followers = models.IntegerField()
 following = models.IntegerField()
 bio = models.CharField(max_length=200)
 likes = models.CharField(max_length=100)
