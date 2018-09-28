import sqlite3


def validateTrainingData(csv_data):
	if not csv_data[6] or not csv_data[12]:
		return False
	return True

def validateTestingData(csv_data):
	if not csv_data[5] or not csv_data[9] or not csv_data[11]:
		return False
	return True

def createTrainingTable(csv_data):
	db = sqlite3.connect('../data/database.db')
	conn = db.cursor()
	
	# create table
	conn.execute('''CREATE TABLE IF NOT EXISTS training_passengers(id INTEGER PRIMARY KEY, survived INTEGER, boarding_class INT,
		name TEXT, gender INTEGER, age INTEGER, sibling_count INTEGER, parent_child_count INTEGER,
		fare REAL, embarked TEXT)''')

	# insert data
	f = open(csv_data)
	f.readline() # skip schema line
	for line in f:
		line = line.rstrip()
		data = line.split(',')
		if not validateTrainingData(data):
			continue
		survived = int(data[1])
		boarding_class = int(data[2])
		name = data[3] + data[4]
		if data[5] == 'male':
			gender = 1
		else:
			gender = 0
		age = float(data[6])
		sibling_count = int(data[7])
		parent_child_count = int(data[8])
		fare = float(data[10])
		embarked = data[12]
		print data
		conn.execute('''INSERT INTO training_passengers(survived, boarding_class, name, gender, age,
			sibling_count, parent_child_count, fare, embarked) VALUES(?,?,?,?,?,?,?,?,?)''', 
			(survived, boarding_class, name, gender, age, sibling_count, parent_child_count, fare, embarked))
	db.commit()
	db.close()

def createTestTable(csv_data):
	db = sqlite3.connect('../data/database.db')
	conn = db.cursor()

	# create table
	conn.execute('''CREATE TABLE IF NOT EXISTS test_passengers(id INTEGER, boarding_class INTEGER,
		name TEXT, gender INTEGER, age INTEGER, sibling_count INTEGER, parent_child_count INTEGER,
		fare REAL, embarked TEXT)''')

	# insert data
	f = open(csv_data)
	f.readline() # skip schema line
	for line in f:
		line = line.rstrip()
		data = line.split(',')
		if not validateTestingData(data):
			continue
		print data
		id = int(data[0])
		boarding_class = int(data[1])
		name = data[2] + data[3]
		if data[4] == 'male':
			gender = 1
		else:
			gender = 0
		age = float(data[5])
		sibling_count = int(data[6])
		parent_child_count = int(data[7])
		fare = float(data[9])
		embarked = data[11]
		
		conn.execute('''INSERT INTO test_passengers(id, boarding_class, name, gender, age,
			sibling_count, parent_child_count, fare, embarked) VALUES(?,?,?,?,?,?,?,?,?)''', 
			(id, boarding_class, name, gender, age, sibling_count, parent_child_count, fare, embarked))
	db.commit()
	db.close()

if __name__ == "__main__":
	createTrainingTable('../data/train.csv')
	createTestTable('../data/test.csv')


