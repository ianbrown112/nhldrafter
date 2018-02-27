from django.db import models

from django.db import models
from teams.models import Team
# Create your models here.

class Player(models.Model):
	team				= models.ForeignKey(Team, on_delete=models.CASCADE)
	name 				= models.CharField(max_length=120)
	
	forward_pos			= models.BooleanField()
	defence_pos			= models.BooleanField()
	rightwing_pos		= models.BooleanField()
	leftwing_pos		= models.BooleanField()
	centre_pos			= models.BooleanField()
	goalie_pos			= models.BooleanField()

	games_played		= models.IntegerField()
	points				= models.IntegerField()
	goals 				= models.IntegerField()
	assists				= models.IntegerField()
	pp_goals			= models.IntegerField()
	pp_assists			= models.IntegerField()
	pp_points			= models.IntegerField()
	gw_goals			= models.IntegerField()
	sh_goals			= models.IntegerField()
	blocks				= models.IntegerField()
	hits				= models.IntegerField()
	faceoff_wins		= models.IntegerField()
	shots               = models.IntegerField(default=0)

	#goalie fields
	games_started		= models.IntegerField(default=0)
	wins 				= models.IntegerField(default=0)
	losses				= models.IntegerField(default=0)
	overtime_losses		= models.IntegerField(default=0)
	shots_against		= models.IntegerField(default=0)
	saves				= models.IntegerField(default=0)
	save_percentage		= models.DecimalField(default=0, decimal_places=3, max_digits=10)
	goals_against_avg	= models.DecimalField(default=0, decimal_places=2, max_digits=10)
	shut_outs			= models.IntegerField(default=0)

	def __str__(self):
		return self.name