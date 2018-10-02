# Titanic Death Predictor
### Predicting passenger survival during the sinking of the titanic using naive-bayes.

The Titanic Death Predictor is a queryable JSON restAPI with a trained naive-bayes model using passenger survival data from 800+ passengers on the Titanic.

The trained model will let you predict whether or not a passenger, not from the training data set, survived. The user can do this by looking at the individuals from the pre-existing test data set (in the test_passenger SQLite3 database table, or via the API), or they can submit their own hypothetical passenger to see whether the model predicts survival or death.

Currently the model is predicting that all 331 valid test passengers survive. This is most likely a math error or a poorly trained model. Fortunately, we can examine ways to tune the model to make it better! Because _this is not a black box naive-bayes implementation_, the user can go to the auditPassenger endpoint, and see all of the numeric values that go into the calculation.

Data is from [Kaggle](https://www.kaggle.com/c/titanic/data)

## Setup

    $ git clone https://github.com/zachjanicki/titanic_death_predictor.git 
    $ cd titanic_death_predictor
    $ pip install virtualenv
    $ virtualenv venv
    $ source venv/bin/activate

    $ pip install -r requirements.txt
    $ cd scripts
    $ python create_database.py

## Usage: 

    `$ ./run.sh`
    
This will start your Flask application and make it locally accessible at `http://127.0.0.1/`


API Endpoints:

* `GET api_V_0_1/data`
  
  - `output: list of all data in database from both test_passenger and training_passenger tables`

* `GET api_V_0_1/data/calculateSurvivalTotals`
       
   - `output: {"survived": int, "perished": int}`

* `GET api_V_0_1/data/didPassengerSurvive/<int:passenger_id>`
        
   - `input: integer passenger_id`
   - `output: {"did_survive": bool}`

* `GET api_V_0_1/data/auditPassenger/<int:passenger_id>`
        
   - ` input: integer passenger_id`
   - `output: a large json object ` see an example [here](https://pastebin.com/p7MCfQSF) 

* `POST api_V_0_1/data/newPassenger`
   
   ```
   request schema:
   {
        "boarding_class": {"type": "number"},
        "name": {"type": "string"},
        "gender": {"type": "string"},
        "age": {"type": "number"},
        "sibling_count": {"type": "number"},
        "parent_child_count": {"type": "number"},
        "fare": {"type": "number"},
        "embarked": {"type": "string"}
    }


## TODO List:

- Make individual test IDs auditable -- DONE

- Put data into queryable database -- DONE

- Create ability to stream data into model -- Post requests supported via REST API, not yet added to persistent store

- Turn into webpage -- Made into REST API

- Dockerize

- Unit Tests

- Deal with error return codes properly (e.g. 404 instead of default error message)

- Robust data validity checking for `POST /data/newPassenger` endpoint

- Create endpoint for user to tune model (e.g. give different factors weights, etc...)



