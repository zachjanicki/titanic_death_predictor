from flask import Flask, request
import json
import sqlite3

from Model import Model

# model setup
with open('config/config.json') as config:
	config_json = json.load(config)

model = Model()
db = sqlite3.connect(config_json['config']['database'])
model.train(db)
db.close()

# api setup
app = Flask(__name__)

@app.route('/')
def helloWorld():
	return 'Hello, World!'

@app.route('/data', methods=['GET'])
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

@app.route('/data/calculateSurvivalTotals')
def calculateSurvivalTotals():
	db = sqlite3.connect(config_json['config']['database'])
	if request.method == 'GET':
		output = {}
		output['survived'], output['perished'] = model.calculateSurvivalTotalFromTestData(db)
		db.close()
		return json.dumps(output)