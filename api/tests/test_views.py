from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..serializers import PostSerializer
from ..models import Post
import json

# API Client app initialized
client = Client()

# demo data 1
def create_post_1():
	return Post.objects.create(username='@Vinicios',
							title='Benefits of serverless infrastructure',
							content='Less time spent deploying, more profit.'
							)
# demo data 2
def create_post_2():
	return Post.objects.create(username='@Victor',
							title='Lorem ipsum dolor sit amet',
							content='Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
							)


# test case for HTTP GET Method
class GetMethodPostApiTest(TestCase):
	# create demo data
	def setUp(self):
		self.post1 = create_post_1()
		self.post2 = create_post_2()

	# get all posts
	def test_get_all_posts(self):
		# get API response
		response = client.get(reverse('post-list'))

		# get data from database
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)

		# sanity check
		# print('\n', response.data, '\n', serializer.data, '\n')

		# compare results
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	# get a specific valid post
	def test_get_valid_single_post(self):
		# get API response
		response = client.get(reverse('post-detail', kwargs={'pk': self.post1.id}))

		# get data from database
		post = Post.objects.get(pk=self.post1.pk)
		serializer = PostSerializer(post)

		# sanity check
		# print('\n', response.data, '\n', serializer.data, '\n')

		# compare results
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	# get specific invalid post
	def test_get_invalid_single_post(self):
		# get API response
		response = client.get(reverse('post-detail', kwargs={'pk': 7}))

		# sanity check
		# print('\n', response.data, '\n')

		# compare result
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# test case for HTTP Post Method
class PostMethodPostApiTest(TestCase):
	def setUp(self):
		self.valid_post = {
			'username': '@Mark',
			'title': 'Title test',
			'content': 'Content test',
		}

		self.invalid_post_list = [
			{# username without '@'
				'username': 'Mark',
				'title': 'Title test',
				'content': 'Content test',
			},
			{# username empty
				'username': '',
				'title': 'Title test',
				'content': 'Content test',
			},
			{# title empty
				'username': '@Mark',
				'title': '',
				'content': 'Content test',
			},
			{# content empty
				'username': '@Mark',
				'title': 'Title test',
				'content': '',
			},
			{  # empty dict
			}
		]

	# create valid object
	def test_create_valid_post(self):
		# get API response
		response = client.post(
			reverse('post-list'),
			data=json.dumps(self.valid_post),
			content_type='application/json'
		)
		# sanity check
		# print('\n', response.data, '\n')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	# create invalid post object
	def test_create_invalid_post(self):
		for post in self.invalid_post_list:
			# get API response
			response = client.post(
				reverse('post-list'),
				data=json.dumps(post),
				content_type='application/json'
			)
			# sanity check
			# print('\n', response.data, '\n')
			self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	# HTTP Post request to detail path
	def test_post_request_wrong_path(self):
		# get API response
		response = client.post(
			reverse('post-detail', kwargs={'pk': 1}),
			data=json.dumps(self.valid_post),
			content_type='application/json'
		)
		# sanity check
		# print('\n', response.data, '\n')
		self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)



# test case for HTTP PUT Method
class PutMethodPostApiTest(TestCase):
	def setUp(self):
		# create demo data
		self.post1 = create_post_1()
		self.post2 = create_post_2()

		self.valid_post = {
			'username': create_post_1().username,
			'title': 'Another title test',
			'content': 'Another content test',
		}

		self.invalid_post_list = [
			{# change username
				'username': '@Another User',
				'title': 'Title test',
				'content': 'Content test',
			},
			{# username empty
				'username': '',
				'title': 'Title test',
				'content': 'Content test',
			},
			{# title empty
				'username': create_post_1().username,
				'title': '',
				'content': 'Content test',
			},
			{# content empty
				'username': create_post_1().username,
				'title': 'Title test',
				'content': '',
			},
			{  # empty dict
			}
		]

	# valid update object
	def test_update_valid_post(self):
		# get API response
		response = client.put(
			reverse('post-detail', kwargs={'pk': self.post1.pk}),
			data=json.dumps(self.valid_post),
			content_type='application/json'
		)
		# sanity check
		# print('\n', response.data, '\n')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	# create invalid post object
	def test_update_invalid_post(self):
		for post in self.invalid_post_list:
			# get API response
			response = client.put(
				reverse('post-detail', kwargs={'pk': self.post1.pk}),
				data=json.dumps(post),
				content_type='application/json'
			)
			# sanity check
			print('\n', response.data, '\n')
			self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	# HTTP PUT request to / path
	def test_put_request_wrong_path(self):
		# get API response
		response = client.put(
			reverse('post-list'),
			data=json.dumps(self.valid_post),
			content_type='application/json'
		)
		# sanity check
		# print('\n', response.data, '\n')
		self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)