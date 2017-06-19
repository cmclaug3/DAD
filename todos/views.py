# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from todos.models import Item

# Create your views here.

def todos(request):
	context = {
		'all_of_them': Item.objects.all
	}
	return render(request, 'todos.html', context)