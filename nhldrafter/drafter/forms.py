from django import forms
from django.shortcuts import get_object_or_404
from django.forms import ModelChoiceField


from players.models import Player
from squads.models import Squad

class SquadForm(forms.ModelForm):
    
    class Meta:
        model = Squad
        fields = ['players', ]
    
    def __init__(self, *args, **kwargs):
    	super(SquadForm, self).__init__(*args, **kwargs)
    	self.fields['players'].label = ''
    	self.fields['players'].queryset = Player.objects.all().order_by('-points')
    	self.fields['players'].label_from_instance = lambda obj: "%s" % obj.name + ", " + str(obj.points) + ", " + obj.team.shortform
    	self.fields['players'].widget.attrs['cols'] = 150