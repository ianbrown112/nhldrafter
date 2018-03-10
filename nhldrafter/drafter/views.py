from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView

from leagues.models import League
from squads.models import Squad
from players.models import Player
from teams.models import Team
from drafter.models import Drafter

from .forms import PlayerForm, TeamForm

# class DraftView(UpdateView):
# 	form_class = PlayerForm
# 	template_name = 'drafter/draft.html'
# 	# def get(self, request, *args, **kwargs):
# 	# 	return render(request, 'drafter/draft.html', context=self.get_context_data())

# 	# def get_queryset(self, *args, **kwargs):
# 	# 	slug = self.kwargs.get('slug')
# 	# 	queryset = League.objects.filter(slug=slug)
# 	# 	return queryset

# 	# def get_context_data(self, *args, **kwargs):
# 	# 	context = super(DraftView, self).get_context_data(**kwargs)
# 	# 	league = self.get_queryset().first()
# 	# 	squads = Squad.objects.filter(league=league)
# 	# 	#context['league'] = league
# 	# 	context['squads'] = squads
# 	# 	return context

# 	# def post(self, request, *args, **kwargs):
# 	# 	league = self.get_queryset().first()

# 	# 	if 'filter' in request.POST:
# 	# 		print(request.POST)
# 	# 		position = request.POST['position']
# 	# 		print(position)
# 	# 		return redirect('/leagues/%s/drafter/%s' % (league.slug, position))
# 	# 	elif 'draft' in request.POST:
# 	# 		squad = Squad.objects.filter(owner=self.request.user).first()
# 	# 		player = request.POST.get('players')
# 	# 		squad.players.add(player)
# 	# 		squad.save()
# 	# 		#instance.save()
# 	# 		return redirect('/leagues/%s/drafter/' % league.slug)

class DraftView(UpdateView):
	
	player_form = PlayerForm()
	team_form = TeamForm

	def get_context_data(self, *args, **kwargs):
		context = super(DraftView, self).get_context_data(**kwargs)
		league = self.get_queryset().first()
		squads = Squad.objects.filter(league=league)
		context['league'] = league
		context['squads'] = squads
		print(context)
		return context
	
	def get_queryset(self, *args, **kwargs):
		slug = self.kwargs.get('slug')
		queryset = League.objects.filter(slug=slug)
		return queryset
	
	def post(self, request, *args, **kwargs):
		team_form = TeamForm
		player_form = PlayerForm()
		league = self.get_queryset().first()
		squads = Squad.objects.filter(league=league)
		drafter = Drafter.objects.filter(league=league)[0]
		
		if 'team_filter' in request.POST:	
			print('team_filter')
			team = Team.objects.filter(name=request.POST['name']).first()
			player_form = player_form.filter_by_position(team.shortform)
			return render(request, 'drafter/draft.html', {	'team_form':team_form, 
															'player_form':player_form, 
															'league':league, 
															'squads':squads}
														)

		elif 'f_filter' in request.POST:	
			player_form = player_form.filter_by_position('F')
			return render(request, 'drafter/draft.html', {	'team_form':team_form, 
															'player_form':player_form, 
															'league':league, 
															'squads':squads}
														)

		elif 'd_filter' in request.POST:	
			player_form = player_form.filter_by_position('D')
			return render(request, 'drafter/draft.html', {	'team_form':team_form, 
															'player_form':player_form, 
															'league':league, 
															'squads':squads}
														)

		elif 'g_filter' in request.POST:	
			player_form = player_form.filter_by_position('G')
			return render(request, 'drafter/draft.html', {	'team_form':team_form, 
															'player_form':player_form, 
															'league':league, 
															'squads':squads}
														)
		
		elif 'draft' in request.POST:
			draft_turn = drafter.draft_turn
			squad 	= Squad.objects.filter(owner=self.request.user).first()
			if draft_turn == squad.draft_order:
				drafter.increase_draft_turn()
				drafter.save()
				league 	= self.get_queryset().first()
				player = Player.objects.filter(name=request.POST.get('name')).first()
				squad.players.add(player)
				squad.save()
				#instance.save()
				return redirect('/leagues/%s/drafter/' % league.slug)

		return redirect('/leagues/%s/drafter/' % league.slug)
		# else:
		# 	player = request.POST.get('players')
		# 	squad = Squad.objects.filter(owner=self.request.user).first()

	def get(self, request, *args, **kwargs):
		league = self.get_queryset().first()
		squads = Squad.objects.filter(league=league)
		player_form = PlayerForm()
		team_form = TeamForm
		return render(request, 'drafter/draft.html', {'team_form':team_form, 'player_form':player_form, 'league':league, 'squads':squads })

def draft_view_filtered(request, slug, *args, **kwargs):
	
	position = kwargs.get('position')
	player_form = PlayerForm()
	player_form = player_form.filter_by_position(position)
	team_form = TeamForm
	#form.filter_by_position(position)
	
	return render(request, 'drafter/draft.html', {'team_form':team_form, 'player_form':player_form })
# class DraftFilterView(UpdateView):
# 	form_class = PlayerForm
# 	template_name = 'drafter/draft.html'

# 	def get_queryset(self, *args, **kwargs):
# 		slug = self.kwargs.get('slug')
# 		position = self.kwargs.get('position')
# 		if position == 'F':
# 			queryset = Player.objects.filter(forward_pos=True)
# 		elif position == 'D':
# 			queryset = Player.objects.filter(defence_pos=True)
# 		return queryset

# 	def get_context_data(self, *args, **kwargs):
# 		context = super(DraftFilterView, self).get_context_data(**kwargs)
# 		league = self.get_queryset().first()
# 		squads = Squad.objects.filter(league=league)
# 		context['league'] = league
# 		context['squads'] = squads
# 		return context

