# this file is used solely for testing
import requests
import json

LOCAL_HOST_URL='http://127.0.0.1:5000'
payload = {
	'boarding_class': '1',
	'name': '',
	'gender': 'male',
	'age': '23',
	'sibling_count': '2',
	'parent_child_count': '2',
	'fare': '12.43',
	'embarked': 'southampton'
	}
r = requests.post(url=LOCAL_HOST_URL + '/data/newPassenger', json=payload)
        