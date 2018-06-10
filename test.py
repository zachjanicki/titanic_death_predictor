def testModel(model, csv_testing_file):
	# Inputs::
	#	dict -- model
	#	string -- csv_testing_file
	# Outputs::
	#	

	f = open(csv_testing_file)
	f.readline()
	output_data = {}

	for line in f:
		data = line.split(',')
		if not validateData(data):
			print 'insufficient passenger data'
			return None
		p_survival = calculateSurvival(model, data)
		p_death = calculateDeath(model, data)
		if p_survival > p_death: # yay!
			print 'passenger {}, {} {}, survived!'.format(data[0], data[3], data[2])
		else: 
			print 'passenger {}, {} {}, did not survive'.format(data[0], data[3], data[2])

def calculateSurvival(model, data):
	# Inputs::
	#	dict -- model
	#	list -- data // preseparated line of csv data from csv_testing_file
	# Outputs::
	#	double -- p_survival
	
	survival_count = model['passenger_count'] - model['survivals']
	passenger_class = model['passenger_class'][int(data[1])]
	p_class = passenger_class / survival_count

	if data[4] == 'male':
		gender = model['gender']['male']
	else:
		gender = model['gender']['female']
	p_gender = gender / survival_count


def validateData(csv_data):
	if not csv_data[6]:
		return False
	return True
