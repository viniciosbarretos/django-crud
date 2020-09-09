from django.db import models
from .validators import username_validator

class Post(models.Model):
	# ID is automatically generated and not editable by default
	username = models.CharField(max_length=140, help_text='', validators=[username_validator])

	# post data
	title = models.CharField(max_length=140, help_text='')
	content = models.TextField(help_text='')

	# datetime generated automatically
	created_datetime = models.DateTimeField(auto_now_add=True, editable=False)

	def __str__(self):
		return self.title

	class Meta:
		# sort (descending order) posts based on creation datetime
		ordering = ('-created_datetime',)