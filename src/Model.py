from Passenger import Passenger
from TrainingDataPassenger import TrainingDataPassenger

class Model(object):
	def __init__(self):
		self.passenger_count = 0
		self.deaths = 0
		self.survivals = 0
		self.passenger_class_survival_count = {1: 0, 2: 0, 3: 0}
		self.gender_survival_count = {1: 0, 0: 0} # 1 for male, 0 for female
		self.age_survival_count = {'minor': 0, 'adult': 0, 'senior': 0} # currently defined as 0-18, 19-64, 65+
		self.sibling_count_survival_count = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
		self.parent_child_count_survival_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
		self.fare = 0
		self.embarked_location_survival_count = {'C': 0, 'Q': 0, 'S': 0} # cherbourg, queenstown, southampton
		self.passenger_list = []
		self.survivals_test_total = 0
		self.deaths_test_total = 0
	
	def train(self, database):
		conn = database.cursor()
		conn.execute('''SELECT * FROM training_passengers''')
		all_passengers = conn.fetchall()
		for p in all_passengers:
			id = p[0]
			survived = p[1]
			boarding_class = p[2]
			name = p[3]
			gender = p[4]
			age = p[5]
			sibling_count = p[6]
			parent_child_count = p[7]
			fare = p[8]
			embarked = p[9]
			current_passenger = TrainingDataPassenger(id, survived, boarding_class, name,
				gender, age, sibling_count, parent_child_count, fare, embarked)
			self.loadPassenger(current_passenger)

	def loadPassenger(self, passenger):
		# Inputs::
		#	passenger -- Passenger()
		# Outputs::
		#	None -- model is modified
		self.passenger_list.append(passenger)
		self.passenger_count += 1
		if passenger.survived:
			self.survivals += 1
			self.passenger_class_survival_count[passenger.boarding_class] += 1
			self.gender_survival_count[passenger.gender] += 1
			self.age_survival_count[passenger.age] += 1
			self.sibling_count_survival_count[passenger.sibling_count] += 1
			self.parent_child_count_survival_count[passenger.parent_child_count] += 1
			self.fare += passenger.fare
			self.embarked_location_survival_count[passenger.embarked] += 1
		else: 
			self.deaths += 1

	def calculateSurvivalTotalFromTestData(self, database):
		conn = database.cursor()
		conn.execute('''SELECT * FROM test_passengers''')
		all_passengers = conn.fetchall()
		for passenger in all_passengers:
			
			test_passenger_class = passenger[1]
			test_passenger_name = passenger[2]
			test_passenger_gender = passenger[3]
			test_passenger_age = passenger[4]
			test_sibling_count = passenger[5]
			test_parent_sibling_count = passenger[6]
			test_fare = passenger[7]
			test_embarked = passenger[8]

			p = Passenger(test_passenger_class, test_passenger_name, test_passenger_gender, test_passenger_age,
				test_sibling_count, test_parent_sibling_count, test_fare, test_embarked)
			if self.didPassengerSurvive(p):
				self.survivals_test_total += 1
			else:
				self.deaths_test_total += 1

		return self.survivals_test_total, self.deaths_test_total


	def auditPassengerSurvivalChance(self, database, passenger_id):
		conn = database.cursor()
		conn.execute('''SELECT * FROM test_passengers WHERE id={}'''.format(passenger_id))
		passenger = conn.fetchone()

		test_passenger_class = passenger[1]
		test_passenger_name = passenger[2]
		test_passenger_gender = passenger[3]
		test_passenger_age = passenger[4]
		test_sibling_count = passenger[5]
		test_parent_sibling_count = passenger[6]
		test_fare = passenger[7]
		test_embarked = passenger[8]
		p = Passenger(test_passenger_class, test_passenger_name, test_passenger_gender, test_passenger_age,
				test_sibling_count, test_parent_sibling_count, test_fare, test_embarked)

	def didPassengerSurvive(self, passenger):
		# P(class | survival)
		p_class_survival_prob = float(passenger.boarding_class) / float(self.survivals)
		p_class_death_prob = float(passenger.boarding_class) / float(self.deaths)

		# P(gender | survival)
		if passenger.gender:
			p_gender_survival_prob = float(self.gender_survival_count[1]) / float(self.survivals)
			p_gender_death_prob = float(self.gender_survival_count[1]) / float(self.deaths)
		else:
			p_gender_survival_prob = float(self.gender_survival_count[0]) / float(self.survivals)
			p_gender_death_prob = float(self.gender_survival_count[0]) / float(self.deaths)

		# P(age | survival)
		if passenger.age <= 18:
			p_age_survival_prob = float(self.age_survival_count['minor']) / float(self.survivals)
			p_age_death_prob = float(self.age_survival_count['minor']) / float(self.deaths)
		elif passenger.age > 18 and passenger.age <= 65:
			p_age_survival_prob = float(self.age_survival_count['adult']) / float(self.survivals)
			p_age_death_prob = float(self.age_survival_count['adult']) / float(self.deaths)
		else:
			p_age_survival_prob = float(self.age_survival_count['senior']) / float(self.survivals)
			p_age_death_prob = float(self.age_survival_count['senior']) / float(self.deaths)
		
		# P(sibling count | survival)
		p_sibling_count_survival_prob = float(passenger.sibling_count) / float(self.survivals)
		p_sibling_count_death_prob = float(passenger.sibling_count) / float(self.deaths)
		
		# P(parent/child count | survival)
		p_parent_sibling_count_survival_prob = float(passenger.parent_child_count) / float(self.survivals)
		p_parent_sibling_count_death_prob = float(passenger.parent_child_count) / float(self.deaths)

		# P(port | survival)
		if passenger.embarked == 'C':
			p_embarked_survival = float(self.embarked_location_survival_count['C']) / float(self.survivals)
			p_embarked_death = float(self.embarked_location_survival_count['C']) / float(self.deaths)
		elif passenger.embarked == 'Q':
			p_embarked_survival = float(self.embarked_location_survival_count['Q']) / float(self.survivals)
			p_embarked_death = float(self.embarked_location_survival_count['Q']) / float(self.deaths)
		else:
			p_embarked_survival = float(self.embarked_location_survival_count['S']) / float(self.deaths)
			p_embarked_death = float(self.embarked_location_survival_count['S']) / float(self.deaths)
		p_survival = p_class_survival_prob * p_gender_survival_prob * p_sibling_count_survival_prob * p_parent_sibling_count_survival_prob * p_embarked_survival
		p_death = p_class_death_prob * p_gender_death_prob * p_sibling_count_death_prob * p_parent_sibling_count_death_prob * p_embarked_death

		if p_survival > p_death: #yay!
			return True
		else: # :(
			return False

