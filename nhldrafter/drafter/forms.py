from django import forms
from django.shortcuts import get_object_or_404
from django.forms import ModelForm, ChoiceField


from players.models import Player
from squads.models import Squad
from teams.models import Team


def make_player_tuple(queryset):
	result = []
	for player in queryset:
		player_tuple = (player, player.name + ', ' + str(player.points) + ', ' + player.team.shortform)
		result.append(player_tuple)
	return result

def make_team_tuple(queryset):
	result = []
	for team in queryset:
		team_tuple = (team, team.shortform)
		result.append(team_tuple)
	return result

players 		= Player.objects.all().order_by('-points')
player_options 	= make_player_tuple(players)

teams 			= Team.objects.all()
team_options 	= make_team_tuple(teams)


class PlayerForm(forms.Form):
	options = player_options
	name = forms.ChoiceField(choices=options)

	class Meta:
		ordering = ['points']

	def __init__(self, *args, **kwargs):
		super(PlayerForm, self).__init__(*args, **kwargs)
		self.fields['name'].label 				= ''
		self.fields['name'].queryset 			= Player.objects.all().order_by('-points')
		self.fields['name'].label_from_instance = lambda obj: "%s" % obj.name + ", " + str(obj.points) + ", " + obj.team.shortform

	def filter_by_position(self, *args, **kwargs):
		form = super(PlayerForm, self)
		if args[0]=='F':
			queryset	 				= Player.objects.filter(forward_pos=True).order_by('-points')
			options 					= make_player_tuple(queryset)
			self.fields['name'] 		= forms.ChoiceField(choices=options)
			self.fields['name'].label 	= ''
			print("forward")
			return form

		elif args[0]=='D':
			queryset	 				= Player.objects.filter(defence_pos=True).order_by('-points')
			options 					= make_player_tuple(queryset)
			self.fields['name']         = forms.ChoiceField(choices=options)
			self.fields['name'].label 	= ''
			print("defence")
			return form

		elif args[0]=='G':
			queryset	 				= Player.objects.filter(goalie_pos=True)
			options 					= make_player_tuple(queryset)
			self.fields['name']         = forms.ChoiceField(choices=options)
			self.fields['name'].label 	= ''
			self.fields['name'].label_from_instance = lambda obj: "%s" % obj.name + ", " + obj.wins + " wins, " + str(obj.save_percentage) + ", " + obj.team.shortform
			print("goalie")
			return form	

class TeamForm(forms.Form):
	options = team_options
	name 	= forms.ChoiceField(choices=options)
	
	def __init__(self, *args, **kwargs):
		super(TeamForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = ''
		