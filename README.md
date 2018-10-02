# Titanic Death Predictor
### Predicting passenger survival during the sinking of the titanic using naive-bayes.

The titanic death predictor is a query-able web API with a trained model using passenger survival data from 800+ passengers on the titanic.

Data is from [Kaggle](https://www.kaggle.com/c/titanic/data)

## Setup

    $ git clone https://github.com/zachjanicki/titanic_death_predictor.git
    $ pip install virtualenv
    $ virtualenv venv
    $ source venv/bin/activate

    $ pip install -r requirements.txt

Usage: $ ./run.sh


API Endpoints:

* `GET api_V_0_1/data`
  
  - `output: list of all data in database`

* `GET api_V_0_1/data/calculateSurvivalTotals`
       
 - `output: {"survived": int, "perished": int}`

* `GET api_V_0_1/data/didPassengerSurvive/<int:passenger_id>`
        
   - `input: integer passenger_id`
   - `output: {"did_survive": bool}`

* `GET api_V_0_1/data/auditPassenger/<int:passenger_id>`
        
   - ` input: integer passenger_id`
   - `output: {"did_survive": bool} `

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


TODO List:

- Make individual test IDs auditable -- DONE

- Put data into queryable database -- DONE

- Create ability to stream data into model -- Post requests supported via REST API

- Turn into webpage -- Made into REST API

- Visualize data trends

- Dockerize

- Unit Tests

- Deal with error return codes properly (e.g. 404 instead of default error message)

- Robust postdata validity checking

