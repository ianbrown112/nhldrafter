from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

# Create your views here.
from .models import Squad
from players.models import Player
# Create your views here.
class SquadListView(ListView):
	#Django will automatically look up template based on naming convention
	#ListView will always return object_list
	def get_queryset(self):
		queryset = Squad.objects.all()
		print(queryset)
		return queryset

class SquadDetailView(DetailView):
	def get_queryset(self, *args, **kwargs):
		slug = self.kwargs.get('slug')
		queryset = Squad.objects.filter(slug=slug)
		return queryset

	def get_context_data(self, *args, **kwargs):
		context = super(SquadDetailView, self).get_context_data(**kwargs)
		squad = self.get_queryset().first()
		players = squad.players.all()
		context['players'] = players
		print(context)
		return context

