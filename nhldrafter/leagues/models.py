from django.db import models

from django.conf import settings
from django.template.defaultfilters import slugify
# Create your models here.
User = settings.AUTH_USER_MODEL

class League(models.Model):
	admin 			= models.ForeignKey(User, on_delete=models.CASCADE)
	name			= models.CharField(max_length=120, unique=True)
	slug			= models.SlugField(default="")
	password 		= models.CharField(max_length=100, default="", null=False)
	owner_amount	= models.IntegerField(default=0)
	skater_amount	= models.IntegerField(default=0)
	goalie_amount	= models.IntegerField(default=0)
	is_active		= models.BooleanField(default=False)
	draft_goalies	= models.BooleanField(default=True)
	
	def create_slug(self):
		self.slug = slugify(self.name)
		return self.slug

	def activate(self):
		self.is_active = True

	def __str__(self):
		return self.name