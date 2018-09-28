import sys
import sqlite3
from Model import Model
from train import trainModel
from test import testModel
from audit import audit

def usage():
	print "Usage:"
	print "\tpython main.py <training_data_file> <testing_data_file>"

if __name__ == "__main__":
	if len(sys.argv) != 3:
		usage()
		exit()

	training_data_file = sys.argv[1]
	testing_data_file = sys.argv[2]
	'''
	model = trainModel(training_data_file)
	output = testModel(model, testing_data_file)
	while True:
		audit_id = raw_input('enter a passenger ID to audit (892-1309): ')
		audit(audit_id, output)
	'''

	
	db = sqlite3.connect('data/database.db')
	model = Model()
	model.train(db)
	model.calculateSurvivalTotalFromTestData(db)