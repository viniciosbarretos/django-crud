from django.core.exceptions import ValidationError

def username_validator(username):
	# check if username starts with '@'
	if username[0] != '@':
		raise ValidationError('This field should start with \'@\'.')