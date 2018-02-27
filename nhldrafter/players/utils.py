from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from .models import Player
from teams.models import Team

base_url = 'https://www.hockey-reference.com/teams/' #ANA/2018.html'

def add_roster(base_url, team_shortform):
	
	#get Team object from database
	team = Team.objects.filter(shortform__iexact=team_shortform).first()

	my_url = base_url + team_shortform + '/2018.html'
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")

	skaters = page_soup.findAll("table", {"id":"skaters"})

	skater_rows = skaters[0].tbody.findAll("tr")

	for row in skater_rows:
		result_list 	= []
		name 			= row.a.text
		position 		= row.findAll("td", {"data-stat":"pos"})[0].text
		forward_pos		= False
		defence_pos		= False
		rightwing_pos	= False
		leftwing_pos	= False
		centre_pos		= False
		goalie_pos		= False

		if position == 'C':
			centre_pos = True
			forward_pos = True
		if position == 'LW':
			leftwing_pos = True
			forward_pos = True
		if position == 'RW':
			rightwing_pos = True
			forward_pos = True
		if position == 'D':
			defence_pos = True
		if position == 'G':
			goalie_pos = True
			continue

		games_played	= row.findAll("td", {"data-stat":"games_played"})[0].text
		goals           = row.findAll("td", {"data-stat":"goals"})[0].text
		assists         = row.findAll("td", {"data-stat":"assists"})[0].text
		points          = row.findAll("td", {"data-stat":"points"})[0].text
		goals_pp        = row.findAll("td", {"data-stat":"goals_pp"})[0].text
		goals_sh        = row.findAll("td", {"data-stat":"goals_sh"})[0].text
		goals_gw        = row.findAll("td", {"data-stat":"goals_gw"})[0].text
		assists_pp      = row.findAll("td", {"data-stat":"assists_pp"})[0].text
		pp_points		= goals_pp + assists_pp
		shots           = row.findAll("td", {"data-stat":"shots"})[0].text
		blocks          = row.findAll("td", {"data-stat":"blocks"})[0].text
		if blocks == '':
			blocks = 0
		hits            = row.findAll("td", {"data-stat":"hits"})[0].text  
		faceoff_wins    = row.findAll("td", {"data-stat":"faceoff_wins"})[0].text
		if faceoff_wins == '':
			faceoff_wins = 0
		
		qs = Player.objects.filter(team__shortform__iexact=team_shortform, name__iexact=name)
		if qs.exists():
			continue

		player = Player(team=team, name=name, forward_pos=forward_pos, defence_pos=defence_pos, goalie_pos=goalie_pos,
						rightwing_pos=rightwing_pos, leftwing_pos=leftwing_pos, centre_pos=centre_pos,
						games_played=games_played, goals=goals, assists=assists, points=points,
						pp_goals=goals_pp, sh_goals=goals_sh, gw_goals=goals_gw, pp_assists=assists_pp, pp_points=pp_points,
						shots=shots, blocks=blocks, hits=hits, faceoff_wins=faceoff_wins)

		player.save()

def add_goalies(base_url, team_shortform):
	
	#get Team object from database
	team = Team.objects.filter(shortform__iexact=team_shortform).first()

	my_url = base_url + team_shortform + '/2018.html'
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()
	page_soup = soup(page_html, "html.parser")

	goalies = page_soup.findAll("table", {"id":"goalies"})
	goalie_rows = goalies[0].tbody.findAll("tr")

	for row in goalie_rows:
		forward_pos			= False
		defence_pos			= False
		rightwing_pos		= False
		leftwing_pos		= False
		centre_pos			= False
		goalie_pos			= True
		
		name 				= row.a.text
		games_played 		= row.findAll("td", {"data-stat":"games_goalie"})[0].text
		games_started 		= row.findAll("td", {"data-stat":"starts_goalie"})[0].text
		wins 				= row.findAll("td", {"data-stat":"wins_goalie"})[0].text
		losses 				= row.findAll("td", {"data-stat":"losses_goalie"})[0].text
		overtime_losses		= row.findAll("td", {"data-stat":"ties_goalie"})[0].text
		shots_against		= row.findAll("td", {"data-stat":"shots_against"})[0].text
		saves				= row.findAll("td", {"data-stat":"saves"})[0].text
		save_percentage		= row.findAll("td", {"data-stat":"save_pct"})[0].text
		goals_against_avg	= row.findAll("td", {"data-stat":"goals_against_avg"})[0].text
		shut_outs			= row.findAll("td", {"data-stat":"shutouts"})[0].text

		if Player.objects.filter(name__iexact=name, team__shortform__iexact=team_shortform).exists():
			player 						= Player.objects.filter(name__iexact=name, team__shortform__iexact=team_shortform)[0]
			player.games_played 		= games_played
			player.games_started 		= games_started
			player.wins 				= wins
			player.losses 				= losses
			player.overtime_losses		= overtime_losses
			player.shots_against		= shots_against
			player.saves				= saves
			player.save_percentage		= save_percentage
			player.goals_against_avg	= goals_against_avg
			player.shut_outs			= shut_outs
			print(name + " already in db")
			#player.save()

		else:
			player = Player(team=team, name=name, forward_pos=forward_pos, defence_pos=defence_pos, goalie_pos=goalie_pos,
							rightwing_pos=rightwing_pos, leftwing_pos=leftwing_pos, centre_pos=centre_pos,
							games_played=games_played, games_started=games_started, wins=wins, losses=losses,
							overtime_losses=overtime_losses, shots_against=shots_against, saves=saves,
							save_percentage=save_percentage, goals_against_avg=goals_against_avg, shut_outs=shut_outs,
							goals=0, assists=0, points=0, pp_goals=0, sh_goals=0, gw_goals=0, pp_assists=0, pp_points=0,
							shots=0, blocks=0, hits=0, faceoff_wins=0)
			print(name + " not already in db")
			player.save()
			print("player saved")