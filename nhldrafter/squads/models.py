from django.db import models

from django.conf import settings

from players.models import Player
from leagues.models import League

User = settings.AUTH_USER_MODEL

# Create your models here.
class Squad(models.Model):
	
	owner 		= models.ForeignKey(User, on_delete=models.CASCADE)
	league		= models.ForeignKey(League, on_delete=models.CASCADE)
	players		= models.ManyToManyField(Player, related_name="on_squad", blank=True)
	name		= models.CharField(max_length=120)
	draft_order	= models.IntegerField(default=0)

	slug		= models.SlugField(default=name)

	def __str__(self):
		return self.name