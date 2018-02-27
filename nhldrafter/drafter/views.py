from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView

from leagues.models import League
from squads.models import Squad
from players.models import Player

from .forms import SquadForm

class DraftView(UpdateView):
	form_class = SquadForm
	template_name = 'drafter/draft.html'
	# def get(self, request, *args, **kwargs):
	# 	return render(request, 'drafter/draft.html', context=self.get_context_data())

	def get_queryset(self, *args, **kwargs):
		slug = self.kwargs.get('slug')
		queryset = League.objects.filter(slug=slug)
		print(queryset)
		return queryset

	def get_context_data(self, *args, **kwargs):
		context = super(DraftView, self).get_context_data(**kwargs)
		league = self.get_queryset().first()
		squads = Squad.objects.filter(league=league)
		#context['league'] = league
		context['squads'] = squads
		print(context)
		return context

	def post(self, request, *args, **kwargs):
		squad = Squad.objects.filter(owner=self.request.user).first()
		league = self.get_queryset().first()
		player = request.POST.get('players')
		squad.players.add(player)
		squad.save()
		#instance.save()
		return redirect('/leagues/%s/drafter/' % league.slug)