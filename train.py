import sys

def trainModel(csv_file):
	# Inputs:: 
	#	str -- csv_file
	
	# Outputs:: 
	#	dict -- model
	model = {}
	model['passenger_count'] = 0
	model['survivals'] = 0
	model['passenger_class_survival'] = {1: 0, 2: 0, 3: 0}
	model['passenger_class_death'] = {1: 0, 2: 0, 3: 0}
	model['gender_survival'] = {'male': 0, 'female': 0}
	model['gender_death'] = {'male': 0, 'female': 0}
	model['age_survival'] = {'minor': 0, 'adult': 0, 'senior': 0} # currently defined as 0-18, 19-64, 65+
	model['age_death'] = {'minor': 0, 'adult': 0, 'senior': 0}
	model['sibling_count_survival'] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
	model['sibling_count_death'] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
	model['parent_child_count_survival'] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
	model['parent_child_count_death'] = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
	model['fare'] = 0 # not sure how to break up this category yet... need to examine min/max from data
	model['embarked_survival'] = {'cherbourg': 0, 'queenstown': 0, 'southampton': 0}
	model['embarked_death'] = {'cherbourg': 0, 'queenstown': 0, 'southampton': 0}

	f = open(csv_file)
	f.readline() # skipping schema line
	for line in f:
		model = loadDataIntoModel(model, line)
	return model

def loadDataIntoModel(model, csv_data):
	# Inputs::
	#	str -- csv_data // a line of csv data from the data file
	#	dict -- model 
	# Outputs::
	#	None -- model is modified

	data = csv_data.split(',')
	if not validateData(data): # throw out records that are corrupt or missing useful data
		return model

	model['passenger_count'] += 1
	if int(data[1]) == 1:
		model['survivals'] += 1
		mortality_modifier = '_survival'
	else:
		mortality_modifier = '_death'

	model['passenger_class' + mortality_modifier][int(data[2])] += 1

	model['gender' + mortality_modifier][data[5]] += 1

	age = float(data[6])
	if age <= 18:
		model['age' + mortality_modifier]['minor'] += 1
	elif age > 18 and age <= 65:
		model['age' + mortality_modifier]['adult'] += 1
	else:
		model['age' + mortality_modifier]['senior'] += 1

	if int(data[7]) not in model['sibling_count' + mortality_modifier]:
		model['sibling_count' + mortality_modifier][int(data[7])] = 1
	else:
		model['sibling_count' + mortality_modifier][int(data[7])] += 1

	if int(data[8]) not in model['parent_child_count' + mortality_modifier]:
		model['parent_child_count' + mortality_modifier][int(data[8])] = 1
	else:
		model['parent_child_count' + mortality_modifier][int(data[8])] += 1

	model['fare'] += float(data[10])

	port = data[12].strip()
	if port == 'C':
		model['embarked' + mortality_modifier]['cherbourg'] += 1
	elif port == 'Q':
		model['embarked' + mortality_modifier]['queenstown'] += 1
	elif port == 'S':
		model['embarked' + mortality_modifier]['southampton'] += 1
	return model

def validateData(csv_data):
	if not csv_data[6]:
		return False
	return True