from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View, CreateView

from .forms import LeagueCreateForm
from .models import League
from squads.forms import SquadCreateForm
from squads.models import Squad
from drafter.models import Drafter
# Create your views here.
class LeagueCreateView(CreateView):
	form_class 		= LeagueCreateForm
	template_name 	= 'leagues/create_league.html'

	def get_queryset(self):
		return League.objects.all()

	def post(self, request, *args, **kwargs):
		form = LeagueCreateForm(request.POST)
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
			drafter = Drafter(league=league)
			drafter.save()
			#return render(request, 'leagues/join_league.html', { 'league':league, 'form':SquadCreateForm() })
			return HttpResponseRedirect('/leagues/%s/join/' % league.slug)
# class LeagueJoinView(View):
# 	template_name = 'leagues/join_league.html'
# 	def get(self, request, *args, **kwargs):
# 		slug = kwargs['slug']
# 		return render(request, '/leagues/%s/join_league.html' % slug)

def league_join_view(request, *args, **kwargs):
	form = SquadCreateForm()
	slug = kwargs['slug']
	league = League.objects.filter(slug=slug)[0]
	user = request.user
	if request.POST:
		name = request.POST['name']
		squad = Squad(owner=user, league=league, name=name)
		squad.create_slug()
		squad.save()
		return HttpResponseRedirect('/leagues/%s/drafter/' % league.slug)
	return render(request, 'leagues/join_league.html', { 'league':league, 'form':form })