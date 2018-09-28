from Passenger import Passenger

class TrainingDataPassenger(Passenger):
	def __init__(self, id, survived, boarding_class, name, gender, age, sibling_count, parent_child_count, fare, embarked):
		super(TrainingDataPassenger, self).__init__(boarding_class, name, gender, age, sibling_count, parent_child_count, fare, embarked)
		self.id = id
		self.survived = survived

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
		return '\n'