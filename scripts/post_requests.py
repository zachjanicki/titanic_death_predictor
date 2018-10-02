# this file is used solely for testing
import requests
import json

from collections import OrderedDict

LOCAL_HOST_URL='http://127.0.0.1:5000'

# going this strange tuple to orderedDict route ehre to add future support to the DataValidator class

payload_tuple_list = [('boarding_class', 1), ('name', ''), ('gender', 'male'), ('age', 23),
						('sibling_count', 2), ('parent_child_count', 2), ('fare', 12.43), ('embarked', 'southampton')]

payload = OrderedDict(payload_tuple_list)

r = requests.post(url=LOCAL_HOST_URL + '/api_V_0_1/data/newPassenger', json=payload)
print r.text
        