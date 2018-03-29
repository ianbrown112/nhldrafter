from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView

from leagues.models import League
from squads.models import Squad
from players.models import Player
from teams.models import Team
from drafter.models import Drafter

from .forms import PlayerForm, TeamForm
from .utils import randomize_draft_order

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
		league = self.get_queryset().first()
		squads = Squad.objects.filter(league=league)
		player_form = PlayerForm(squads=squads)
		drafter = Drafter.objects.filter(league=league)[0]
		
		if 'team_filter' in request.POST:	
			print('team_filter')
			team = Team.objects.filter(name=request.POST['name']).first()
			print(team)
			player_form = player_form.filter_by_team(team.shortform)
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
			squad = Squad.objects.filter(owner=self.request.user, league=league).first()
			print(squad.owner)
			print(squad.draft_order)
			print(drafter.draft_turn)
			
			if drafter.is_active:

				if drafter.is_even_round() == False:
					if drafter.draft_turn == squad.draft_order:
						drafter.increase_overall_pick()
						player = Player.objects.filter(name=request.POST.get('name')).first()
						squad.players.add(player)
						squad.save()
						#instance.save()
						if drafter.draft_turn == drafter.turns_per_round:
							drafter.increase_round()
						else:
							drafter.increase_draft_turn()
						
						if drafter.overall_pick == drafter.total_picks + 1:
							drafter.deactivate()

						drafter.save()
					
						return redirect('/leagues/%s/drafter/' % league.slug)
				
				elif drafter.is_even_round() == True:
					if drafter.draft_turn == squad.draft_order:
						drafter.increase_overall_pick()
						player = Player.objects.filter(name=request.POST.get('name')).first()
						squad.players.add(player)
						squad.save()
						#instance.save()
						if drafter.draft_turn == 1:
							drafter.increase_round()
						else:
							drafter.decrease_draft_turn()
						
						if drafter.overall_pick == drafter.total_picks + 1:
							drafter.deactivate()

						drafter.save()
						return redirect('/leagues/%s/drafter/' % league.slug)

			else:
				drafter.deactivate()
				drafter.save()
				return redirect('/leagues/%s/drafter/' % league.slug)

		elif 'activate_league' in request.POST:
			number_of_squads 		= squads.count()
			drafter.turns_per_round = number_of_squads
			if league.draft_goalies == True:
				total_rounds = league.skater_amount + league.goalie_amount
			else:
				total_rounds = league.skater_amount
			drafter.total_rounds = total_rounds
			drafter.total_picks  = total_rounds * number_of_squads
			randomize_draft_order(squads, number_of_squads)
			drafter.activate()
			league.activate()
			drafter.save()
			league.save()
			return redirect('/leagues/%s/drafter/' % league.slug)

		return redirect('/leagues/%s/drafter/' % league.slug)
		# else:
		# 	player = request.POST.get('players')
		# 	squad = Squad.objects.filter(owner=self.request.user).first()

	def get(self, request, *args, **kwargs):
		league 			= self.get_queryset().first()
		squads 			= Squad.objects.filter(league=league)
		drafter 		= Drafter.objects.filter(league=league).first()
		player_form 	= PlayerForm(squads=squads)
		team_form 		= TeamForm
		squad_picking	= None
		if league.is_active:
			squad_picking = Squad.objects.filter(draft_order=drafter.draft_turn, league=league).first()
			print(drafter.draft_turn)
			print(squad_picking)
		return render(request, 
						'drafter/draft.html', 
						{'team_form':team_form, 
						 'player_form':player_form, 
						 'league':league, 
						 'squads':squads,
						 'drafter':drafter, 
						 'squad_picking':squad_picking,
						}
					)
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

