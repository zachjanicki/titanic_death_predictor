# Titanic Death Predictor
Predicting passenger survival during the sinking of the titanic.

Data is from [Kaggle](https://www.kaggle.com/c/titanic/data)

Usage: $ ./run.sh


API Endpoints:

* GET /data
	output: list of all data in database

* GET /data/calculateSurvivalTotals
	output: number of test passengers that survived/perished based on model calculations

* GET /data/didPassengerSurvive/<int:passenger_id>
	input: integer passenger_id 
		note -- 892 <= passenger_id => 1307 
	output: bool did_survive

* GET /data/auditModelResult/<int:passenger_id>
	input: integer passenger_id 
                note -- 892 <= passenger_id => 1307
        output: bool did_survive


TODO List:

- Make individual test IDs auditable -- DONE

- Put data into queryable database -- DONE

- Create ability to stream data into model -- Post requests supported via REST API

- Turn into webpage -- Made into REST API

- Visualize data trends

- Dockerize
