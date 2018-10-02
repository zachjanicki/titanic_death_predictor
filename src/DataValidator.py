import json
from jsonschema import validate, ValidationError


class DataValidator(object):
	def __init__(self):
		with open('config/request_data_schemas.json') as request_data_schemas_json:
			request_data_schemas = json.load(request_data_schemas_json)
		self.new_passenger_post_request = request_data_schemas['new_passenger_post_request']

	def validateNewPassengerPostRequestData(self, data):
		print data
		try:
			print "validating"
			validate(data, self.new_passenger_post_request)
			return True
		except ValidationError as e:
			print "error"
			return False