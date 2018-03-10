from django.db import models

from django.conf import settings
from django.template.defaultfilters import slugify
# Create your models here.
User = settings.AUTH_USER_MODEL

class League(models.Model):
	admin 			= models.ForeignKey(User, on_delete=models.CASCADE)
	name			= models.CharField(max_length=120)
	slug			= models.SlugField(default="league1")
	password 		= models.CharField(max_length=100, default="", null=False)
	skater_amount	= models.IntegerField(default=0)
	goalie_amount	= models.IntegerField(default=0)

	def create_slug(self):
		self.slug = slugify(self.name)
		return self.slug