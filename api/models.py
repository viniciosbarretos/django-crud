from django.db import models


class Post(models.Model):
	# ID is automatically generated and not editable
	username = models.CharField(max_length=140, help_text='', editable=False)

	# post data
	title = models.CharField(max_length=140, help_text='')
	content = models.TextField(help_text='')

	#
	created_datetime = models.DateTimeField(auto_now_add=True, editable=False)

	def __str__(self):
		return self.title
