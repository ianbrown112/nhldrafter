from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import LeagueCreateForm
from .models import League
# Create your views here.
class LeagueCreateView(CreateView):
	form_class 		= LeagueCreateForm
	template_name 	= 'leagues/create_league.html'

	def get_queryset(self):
		return League.objects.all()

	def post(self, request, *args, **kwargs):
		form 			= LeagueCreateForm(request.POST)
		if form.is_valid():
			admin 			= self.request.user
			password 		= form.cleaned_data['password']
			name 			= request.POST.get('name')
			skater_amount 	= request.POST.get('skater_amount')
			goalie_amount	= request.POST.get('goalie_amount')
			league 			= League(
	    						admin=admin, 
	    						name=name,
	    						skater_amount=skater_amount,
	    						goalie_amount=goalie_amount,
	    						password=password
	    					)
			league.create_slug()
			league.save()
			return HttpResponseRedirect('/teams/')