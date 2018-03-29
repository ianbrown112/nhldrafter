from random import shuffle

def randomize_draft_order(squads, number_of_squads):
	draft_picks = [x for x in range(1, number_of_squads+1)]
	shuffle(draft_picks)
	for squad in squads:
		squad.draft_order = draft_picks.pop()
		squad.save()
	