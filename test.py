def testModel(model, csv_testing_file):
	# Inputs::
	#	dict -- model
	#	string -- csv_testing_file
	# Outputs::
	#	

	f = open(csv_testing_file)
	f.readline() # skipping schema line
	output_data = {}
	survival_count = 0
	death_count = 0
	bad_data_count = 0
	for line in f:
		data = line.split(',')
		p_survival, audit_outputs_survival = calculateSurvival(model, data, True)
		p_death, audit_outputs_death = calculateSurvival(model, data, False)
		
		output_data[data[0]] = {}
		output_data[data[0]]['name'] = '{} {}'.format(data[2], data[3])
		output_data[data[0]]['class'] = data[1]
		output_data[data[0]]['gender'] = data[4]
		output_data[data[0]]['age'] = data[5]
		output_data[data[0]]['sibling_count'] = int(data[6])
		output_data[data[0]]['parent_child_count'] = int(data[7])
		port = data[11].strip()
		if port == 'C':
			output_data[data[0]]['port'] = 'cherbourg'
		elif port == 'Q':
			output_data[data[0]]['port'] = 'queenstown'
		else:
			output_data[data[0]]['port'] = 'southampton'


		output_data[data[0]]['survival_chance_audit'] = audit_outputs_survival
		output_data[data[0]]['survival_chance_audit']['p_survival'] = p_survival

		output_data[data[0]]['death_chance_audit'] = audit_outputs_death
		output_data[data[0]]['death_chance_audit']['p_death'] = p_death

		if p_survival > p_death: # yay!
			# print 'passenger {}, {} {}, survived!'.format(data[0], data[3], data[2])
			survival_count += 1
		else: 
			# print 'passenger {}, {} {}, did not survive'.format(data[0], data[3], data[2])
			death_count += 1

	print 'Out of 418 passengers, {} survived and {} did not survive'.format(survival_count, death_count)
	return output_data

def calculateSurvival(model, data, survive_modifier):
	# Inputs::
	#	dict -- model
	#	list -- data // preseparated line of csv data from csv_testing_file
	# Outputs::
	#	double -- p_survival
	
	audit_outputs = {}
	death_count = model['passenger_count'] - model['survivals']
	survival_count = model['passenger_count'] - death_count
	if survive_modifier:
		mortality_modifier = '_survival'
	else:
		mortality_modifier = '_death'
	# P(class | survival)
	passenger_class = model['passenger_class' + mortality_modifier][int(data[1])]
	p_class = divisionHelper(passenger_class, survival_count, death_count, survive_modifier)
	audit_outputs['P(Class | ' + dictKeyNameHelper(survive_modifier) + ')'] = p_class
	
	# P(gender | survival)
	gender_count = model['gender' + mortality_modifier][data[4]]
	p_gender = divisionHelper(gender_count, survival_count, death_count, survive_modifier)
	audit_outputs['P(Gender | ' + dictKeyNameHelper(survive_modifier) + ')'] = p_gender

	# P(age | survival)
	if data[5]:
		passenger_age = float(data[5])
		if passenger_age <= 18:
			age_count = model['age' + mortality_modifier]['minor']
		elif passenger_age > 18 and passenger_age <= 65:
			age_count = model['age' + mortality_modifier]['adult']
		else:
			age_count = model['age' + mortality_modifier]['senior']
		p_age = divisionHelper(age_count, survival_count, death_count, survive_modifier)
	else:
		p_age = 1
	audit_outputs['P(Age | ' + dictKeyNameHelper(survive_modifier) + ')'] = p_age

	# P(sibling count | survival)
	passenger_sib_count = model['sibling_count' + mortality_modifier][int(data[6])]
	p_sib_count = divisionHelper(passenger_sib_count, survival_count, death_count, survive_modifier)
	audit_outputs['P(Sibling Count | ' + dictKeyNameHelper(survive_modifier) + ')'] = p_sib_count

	# P(parent/child count | survival)
	passenger_parent_child_count = model['parent_child_count' + mortality_modifier][int(data[7])]
	p_parent_child_count = divisionHelper(passenger_parent_child_count, survival_count, death_count, survive_modifier)
	audit_outputs['P(Parent/Child Count | ' + dictKeyNameHelper(survive_modifier) + ')'] = p_parent_child_count

	# P(port | survival)
	port = data[11].strip()
	if port == 'C':
		passenger_port = model['embarked' + mortality_modifier]['cherbourg']
	elif port == 'Q':
		passenger_port = model['embarked' + mortality_modifier]['queenstown']
	else:
		passenger_port = model['embarked' + mortality_modifier]['southampton']
	p_port = divisionHelper(passenger_port, survival_count, death_count, survive_modifier)
	audit_outputs['P(Port | ' + dictKeyNameHelper(survive_modifier) + ')'] = p_port

	p_output = p_class * p_gender * p_age * p_sib_count * p_parent_child_count * p_port
	return p_output, audit_outputs


def divisionHelper(p_left, survival_count, death_count, survive_modifier):
	if survive_modifier:
		return p_left / float(survival_count)
	else:
		return p_left / float(death_count)

def dictKeyNameHelper(survive_modifier):
	if survive_modifier:
		return 'Survived'
	else:
		return 'Death'

