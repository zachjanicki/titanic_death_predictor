def divisionHelper(p_left, survival_count, death_count, did_passenger_survive):
	if did_passenger_survive:
		return p_left / float(survival_count)
	else:
		return p_left / float(death_count)