def audit(id, data):
	print '\n'
	print "The survival of passenger {}, {}, has been determined using a naive bayes classification algorithm that takes into consideration the passenger's ticket class, gender, age, number of siblings aboard, number of parents and children aboard, and the port they left from.".format(id, data[id]['name'])
	print "The naive bayes classifier works by determining the passenger's chance of survival or death by multiplying the independent variable classes together and choosing the value that is larger."
	print "Passenger {} was in class {}".format(id, data[id]['class'])
	print "Passenger {} was {}".format(id, data[id]['gender'])
	if data[id]['age']:
		print "Passenger {} was {} years old".format(id, data[id]['age'])
	print "Passenger {} had {} siblings aboard".format(id, data[id]['sibling_count'])
	print "Passenger {} had {} parents and children aboard".format(id, data[id]['parent_child_count'])
	print "Passenger {} left from {}".format(id, data[id]['port'])


	print "The formula for survival is as follows:"
	print "\tP(Survival | Class, Gender, Age, Sibling count, Parent/Child count, Port) which becomes:"
	print "\t\tP(Class | Survived) * P(Gender | Survived) * P(Age | Survived) * P(Sibling count | Survived) * P(Parent/Child count | Survived) * P(Port | Survived)"
	print "\tP(Death | Class, Gender, Age, Sibling count, Parent/Child count, Port)"
	print "\t\tP(Class | Death) * P(Gender | Death) * P(Age | Death) * P(Sibling count | Death) * P(Parent/Child count | Death) * P(Port | Death)"
	print "We then take the greater value which predicts whether or not the passenger survives."
	print "for passenger {} we have the following values:".format(id)
	
	print "\tP(Class | Survived) = {}".format(data[id]['survival_chance_audit']['P(Class | Survived)'])
	print "\tP(Gender | Survived) = {}".format(data[id]['survival_chance_audit']['P(Gender | Survived)'])
	print "\tP(Age | Survived) = {}".format(data[id]['survival_chance_audit']['P(Age | Survived)'])
	print "\tP(Sibling Count | Survived) = {}".format(data[id]['survival_chance_audit']['P(Sibling Count | Survived)'])
	print "\tP(Parent/Child Count | Survived) = {}".format(data[id]['survival_chance_audit']['P(Parent/Child Count | Survived)'])

	print "\tP(Class | Death) = {}".format(data[id]['death_chance_audit']['P(Class | Death)'])
	print "\tP(Gender | Death) = {}".format(data[id]['death_chance_audit']['P(Gender | Death)'])
	print "\tP(Age | Death) = {}".format(data[id]['death_chance_audit']['P(Age | Death)'])
	print "\tP(Sibling Count | Death) = {}".format(data[id]['death_chance_audit']['P(Sibling Count | Death)'])
	print "\tP(Parent/Child Count | Death) = {}".format(data[id]['death_chance_audit']['P(Parent/Child Count | Death)'])

	print "\tP(Survived | Class, Gender, Age, Sibling count, Parent/Child count, Port) = {}".format(data[id]['survival_chance_audit']['p_survival'])
	print "\tP(Death | Class, Gender, Age, Sibling count, Parent/Child count, Port) = {}".format(data[id]['death_chance_audit']['p_death'])

	if data[id]['survival_chance_audit']['p_survival'] > data[id]['death_chance_audit']['p_death']:
		print "\t\tTherefore the passenger survives"
	else:
		print "\t\tTherefore the passenger does not survive"
	print '\n'