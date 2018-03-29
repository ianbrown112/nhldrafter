from django.db import models
from leagues.models import League
# Create your models here.
class Drafter(models.Model):
	league 			= models.ForeignKey(League, on_delete=models.CASCADE)
	draft_turn 		= models.IntegerField(default=1)
	turns_per_round	= models.IntegerField(default=0)
	overall_pick	= models.IntegerField(default=1)
	current_round	= models.IntegerField(default=1)
	total_rounds	= models.IntegerField(default=1)
	total_picks		= models.IntegerField(default=0)
	is_active		= models.BooleanField(default=False)

	def activate(self):
		self.is_active = True
		return self.is_active

	def deactivate(self):
		self.is_active = False
		return self.is_active

	def increase_draft_turn(self):
		self.draft_turn += 1
		return self.draft_turn

	def decrease_draft_turn(self):
		self.draft_turn -= 1
		return self.draft_turn

	def increase_overall_pick(self):
		self.overall_pick += 1
		return self.overall_pick

	def decrease_overall_pick(self):
		self.overall_pick -= 1
		return self.overall_pick

	def set_total_rounds(self, positions):
		self.total_rounds = positions
		return self.total_rounds

	def increase_round(self):
		self.current_round += 1
		return self.current_round

	def is_even_round(self):
		if self.current_round%2==0:
			return True 
		else:
			return False