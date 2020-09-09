from django.test import TestCase
from ..models import Post

class PostTest(TestCase):
	# test module for Post model

	def setUp(self):
		Post.objects.create(username='@Vinicios', title='Benefits of serverless infrastructure', content='Less time spent deploying, more profit.')
		Post.objects.create(username='@Victor', title='Lorem ipsum dolor sit amet', content='Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')