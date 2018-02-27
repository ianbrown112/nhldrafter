from django.db import models

# Create your models here.

teams = [
			['Anaheim Ducks', 'ANA'], 
			['Arizona Coyotes', 'ARI'], 
			['Boston Bruins', 'BOS'], 
			['Buffalo Sabres', 'BUF'], 
			['Calgary Flames', 'CGY'], 
			['Carolina Hurricanes', 'CAR'], 
			['Chicago Blackhawks', 'CHI'], 
			['Colorado Avalanche', 'COL'], 
			['Columbus Blue Jackets', 'CBJ'], 
			['Dallas Stars', 'DAL'], 
			['Detroit Red Wings', 'DET'], 
			['Edmonton Oilers', 'EDM'], 
			['Florida Panthers', 'FLA'], 
			['Los Angeles Kings', 'LAK'], 
			['Minnesota Wild', 'MIN'], 
			['Montreal Canadiens', 'MTL'], 
			['Nashville Predators', 'NSH'], 
			['New Jersey Devils', 'NJD'],
			['New York Islanders', 'NYI'], 
			['New York Rangers', 'NYR'], 
			['Ottawa Senators', 'OTT'], 
			['Philadelphia Flyers', 'PHI'], 
			['Pittsburgh Penguins', 'PIT'], 
			['San Jose Sharks', 'SJS'], 
			['St Louis Blues', 'STL'], 
			['Tampa Bay Lightning', 'TBL'], 
			['Toronto Maple Leafs', 'TOR'], 
			['Vancouver Canucks', 'VAN'], 
			['Vegas Golden Knights', 'VEG'], 
			['Washington Capitals', 'WSH'], 
			['Winnipeg Jets', 'WPG']
	]

# Create your models here.
class Team(models.Model):
	
	name		= models.CharField(max_length=120)
	shortform	= models.CharField(max_length=3, null=True)
	in_playoffs	= models.BooleanField(default=False)
	slug		= models.SlugField(default=shortform)

	def __str__(self):
		return self.name