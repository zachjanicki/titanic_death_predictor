import json

class ErrorHandler(object):
	def __init__(self):
		with open('config/error_messages.json') as error_messages_json:
			error_messages = json.load(error_messages_json)
		self.default_error_message = error_messages['default_error']
		self.default_warning_message = error_messages['default_warning']

	def error(self, message=None):
		if not message:
			return {'error': self.default_error_message}
		return {'error': message}

	def warning(self, message=None):
		if not message:
			return {'warning': self.default_warning_message}
		return {'warning': message}