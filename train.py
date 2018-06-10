import sys

def trainModel(csv_file):
	# Inputs:: 
	#	str -- csv_file
	
	# Outputs:: 
	#	dict -- model
	model = {}
	model['passenger_count'] = 0
	model['survivals'] = 0
	model['passenger_class'] = {1: 0, 2: 0, 3: 0}
	model['gender'] = {'male': 0, 'female': 0}
	model['age'] = {'minor': 0, 'adult': 0, 'senior': 0} # currently defined as 0-18, 19-64, 65+
	model['sibling_count'] = {}
	model['parent_child_count'] = {}
	model['fare'] = 0 # not sure how to break up this category yet... need to examine min/max from data
	model['embarked'] = {'cherbourg': 0, 'queenstown': 0, 'southampton': 0}

	f = open(csv_file)
	f.readline() # skipping schema line
	for line in f:
		model = loadDataIntoModel(line, model)
	return model

def loadDataIntoModel(csv_data, model):
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

	model['passenger_class'][int(data[2])] += 1

	model['gender'][data[5]] += 1

	age = float(data[6])
	if age <= 18:
		model['age']['minor'] += 1
	elif age > 18 and age <= 65:
		model['age']['adult'] += 1
	else:
		model['age']['senior'] += 1

	if int(data[7]) not in model['sibling_count']:
		model['sibling_count'][int(data[7])] = 1
	else:
		model['sibling_count'][int(data[7])] += 1

	if int(data[8]) not in model['parent_child_count']:
		model['parent_child_count'][int(data[8])] = 1
	else:
		model['parent_child_count'][int(data[8])] += 1

	model['fare'] += float(data[10])

	port = data[12].strip()
	if port == 'C':
		model['embarked']['cherbourg'] += 1
	elif port == 'Q':
		model['embarked']['queenstown'] += 1
	elif port == 'S':
		model['embarked']['southampton'] += 1
	else:
		print 'DATA ERROR!'
	return model

def validateData(csv_data):
	if not csv_data[6]:
		return False
	return True

print trainModel('data/train.csv')


