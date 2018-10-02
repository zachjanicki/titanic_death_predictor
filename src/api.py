from flask import Flask, request, abort
from flask_api import FlaskAPI, status
import json
import sqlite3

from Model import Model
from Passenger import Passenger
from ErrorHandler import ErrorHandler
from DataValidator import DataValidator

# model setup
with open('config/config.json') as config:
	config_json = json.load(config)

model = Model()
db = sqlite3.connect(config_json['config']['database'])
model.train(db)
db.close()

error_handler = ErrorHandler()
data_validator = DataValidator()

# api setup
app = Flask(__name__)

@app.route('/api_V_0_1')
def helloWorld():
	return 'Hello, World!'

@app.route('/api_V_0_1/data', methods=['GET'])
def getData():
	db = sqlite3.connect(config_json['config']['database'])
	if request.method == 'GET':
		conn = db.cursor()
		output = {'training_passengers': [], 'test_passengers': []}
		conn.execute('''SELECT * FROM training_passengers''')
		results = conn.fetchall()
		for passenger in results:
			p = {}
			p['id'] = passenger[0]
			p['survived'] = passenger[1]
			p['boarding_class'] = passenger[2]
			p['name'] = passenger[3]
			p['gender'] = passenger[4]
			p['age'] = passenger[5]
			p['sibling_count'] = passenger[6]
			p['parent_child_count'] = passenger[7]
			p['fare'] = passenger[8]
			p['embarked'] = passenger[9]
			output['training_passengers'].append(p)
		conn.execute('''SELECT * FROM test_passengers''')
		results = conn.fetchall()
		for passenger in results:
			p = {}
			p['id'] = passenger[0]
			p['boarding_class'] = passenger[1]
			p['name'] = passenger[2]
			p['gender'] = passenger[3]
			p['age'] = passenger[4]
			p['sibling_count'] = passenger[5]
			p['parent_child_count'] = passenger[6]
			p['fare'] = passenger[7]
			p['embarked'] = passenger[8]
			output['test_passengers'].append(p)
		db.close()
		return json.dumps(output)
	else:
		abort(405)

@app.route('/api_V_0_1/data/calculateSurvivalTotals', methods=['GET'])
def calculateSurvivalTotals():
	db = sqlite3.connect(config_json['config']['database'])
	if request.method == 'GET':
		output = {}
		output['survived'], output['perished'] = model.calculateSurvivalTotalFromTestData(db)
		db.close()
		return json.dumps(output)
	else:
		abort(405)


@app.route('/api_V_0_1/data/didPassengerSurvive/<int:passenger_id>', methods=['GET'])
def didPassengerSurvive(passenger_id):
	if request.method == 'GET':
		db = sqlite3.connect(config_json['config']['database'])
		conn = db.cursor()
		conn.execute('''SELECT * FROM test_passengers WHERE id = {}'''.format(passenger_id))
		passenger = conn.fetchone()
		if not passenger:
			output = error_handler.error("Passenger ID does not exist")
			return json.dumps(output)
		id = passenger[0]
		boarding_class = passenger[1]
		name = passenger[2]
		gender = passenger[3]
		age = passenger[4]
		sibling_count = passenger[5]
		parent_child_count = passenger[6]
		fare = passenger[7]
		embarked = passenger[8]
		p = Passenger(boarding_class, name, gender, age, sibling_count, parent_child_count, fare, embarked)

		output = {}
		output['did_survive'] = model.didPassengerSurvive(p)
		return json.dumps(output)
	else:
		abort(405)

@app.route('/api_V_0_1/data/newPassenger', methods=['POST'])
def createNewTestPassenger():
	if request.method == 'POST':
		if data_validator.validateNewPassengerPostRequestData(request.data):
			print "should fail"
		request_data_as_json = json.loads(request.data)
		boarding_class = request_data_as_json['boarding_class']
		name = request_data_as_json['name']
		gender = request_data_as_json['gender']
		age = request_data_as_json['age']
		sibling_count = request_data_as_json['sibling_count']
		parent_child_count = request_data_as_json['parent_child_count']
		fare = request_data_as_json['fare']
		embarked = request_data_as_json['embarked']
		p = Passenger(boarding_class, name, gender, age, sibling_count, parent_child_count, fare, embarked)
		
		output = {}
		output['did_survive'] = model.didPassengerSurvive(p)
		return json.dumps(output) 
		
		#else:
		#	output = error_handler.error("Post request data is invalid")
		#	return json.dumps(output)
	else:
		abort(405)

















