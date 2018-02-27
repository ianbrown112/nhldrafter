from django.db import models

from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class League(models.Model):
	admin 		= models.ForeignKey(User, on_delete=models.CASCADE)
	name		= models.CharField(max_length=120)
	slug		= models.SlugField(default="league1")