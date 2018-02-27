from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from teams.models import Team
from players.models import Player
# Create your views here.
class TeamListView(ListView):
	#Django will automatically look up template based on naming convention
	#ListView will always return object_list
	def get_queryset(self):
		queryset = Team.objects.all()
		print(queryset)
		return queryset

class TeamDetailView(DetailView):
	def get_queryset(self, *args, **kwargs):
		slug = self.kwargs.get('slug')
		queryset = Team.objects.filter(slug=slug)
		return queryset

	def get_context_data(self, *args, **kwargs):
		context = super(TeamDetailView, self).get_context_data(**kwargs)
		team = self.get_queryset().first()
		players = Player.objects.filter(team=team)
		context['players'] = players
		print(context)
		return context
