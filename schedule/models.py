# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Lesson(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	years_playing = models.IntegerField()
	email = models.EmailField(max_length=50)
	tell_us_about_yourself = models.TextField()
	
	def __str__(self):
		return '{} {}'.format(self.first_name, self.last_name)

		

