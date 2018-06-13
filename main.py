import sys
from train import trainModel
from test import testModel

def usage():
	print "Usage:"
	print "\tpython main.py <training_data_file> <testing_data_file>"

if __name__ == "__main__":
	if len(sys.argv) != 3:
		usage()
		exit()

	training_data_file = sys.argv[1]
	testing_data_file = sys.argv[2]

	model = trainModel(training_data_file)
	output = testModel(model, testing_data_file)
	print output