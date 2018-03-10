"""nhldrafter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from drafter.views import DraftView, draft_view_filtered
from teams.views import TeamListView, TeamDetailView
from squads.views import SquadListView, SquadDetailView
from profiles.views import UserRegisterView, logout_view, login_view
from leagues.views import LeagueCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^register/$', UserRegisterView.as_view(), name="user_register"),
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^leagues/create/$', LeagueCreateView.as_view(), name="create_league"),
    url(r'^leagues/(?P<slug>[\w-]+)/drafter/$', DraftView.as_view(), name="drafter"),
    url(r'^leagues/(?P<slug>[\w-]+)/drafter/(?P<position>[\w-]+)/$', draft_view_filtered, name="drafter_filter"),
    url(r'^teams/$', TeamListView.as_view(), name="team-list"),
    url(r'^teams/(?P<slug>[\w-]+)/$', TeamDetailView.as_view(), name="team-detail"),
    url(r'^squads/$', SquadListView.as_view(), name="squad-list"),
    url(r'^squads/(?P<slug>[\w-]+)/$', SquadDetailView.as_view(), name="squad-detail"),
    url(r'$', TemplateView.as_view(template_name="homepage.html"), name="homepage"),

]
