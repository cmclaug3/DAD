# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
#from django.contrib.auth.models import User

class TestViews(TestCase):
	def setUp(self):
		self.todo = Todo(title='this is a test', text='this is test text!')
		self.todo.save()

	def test_todos(self):
		response = self.client.get(reverse('todos'))
		self.assertEqual(response.status_code, 200)

