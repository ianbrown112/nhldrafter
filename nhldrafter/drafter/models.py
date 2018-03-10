from django.db import models
from leagues.models import League
# Create your models here.
class Drafter(models.Model):
	league 		= models.ForeignKey(League, on_delete=models.CASCADE)
	draft_turn 	= models.IntegerField(default=0)

	def increase_draft_turn(self):
		self.draft_turn += 1
		return self.draft_turn
