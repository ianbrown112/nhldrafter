from django import forms

from .models import Squad

class SquadCreateForm(forms.ModelForm):

	class Meta:
		model 	= Squad
		fields = ['name']
		
	def __init__(self, *args, **kwargs):
		super(SquadCreateForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = 'Squad Name'