# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.contrib.auth.models import User

from django.db import models


PRIORITY_CHOICES = ( 
  	(1, 'Low'), 
  	(2, 'Normal'), 
  	(3, 'High'), 
) 

class Item(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
	completed = models.BooleanField(default=False)
	user = models.ForeignKey(User)

	class Meta: 
		ordering = ['-priority', 'title'] 

	def __str__(self):
		return self.title

