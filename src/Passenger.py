class Passenger(object):
	def __init__(self, boarding_class, name, gender, age, sibling_count, parent_child_count, fare, embarked):
		#self.id = id
		#self.survived = survived
		self.boarding_class = boarding_class
		self.name = name
		self.gender = gender
		if age <= 18:
			self.age = 'minor'
		elif age > 18 and age <= 65:
			self.age = 'adult'
		else:
			self.age = 'senior'
		self.sibling_count = sibling_count
		self.parent_child_count = parent_child_count
		self.fare = fare
		self.embarked = embarked

	def __str__(self):
		print(self.id)
		print(self.survived)
		print(self.boarding_class)
		print(self.name)
		print(self.gender)
		print(self.age)
		print(self.sibling_count)
		print(self.parent_child_count)
		print(self.fare)
		print(self.embarked)
