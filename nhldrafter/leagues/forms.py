from django import forms
from django.shortcuts import get_object_or_404
from django.forms import ModelForm, ChoiceField

from .models import League
class LeagueCreateForm(forms.ModelForm):
	
	class Meta:
		model 	= League
		fields 	= ['name', 'password', 'owner_amount', 'skater_amount', 'goalie_amount', 'draft_goalies']
