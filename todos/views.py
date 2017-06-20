# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from todos.forms import TodoItemForm, CompleteTodoItemForm

from todos.models import Item


@login_required
def todos(request):
	if request.method == 'POST':
		item_id = request.POST.get('id')
		obj = Item.objects.get(id=item_id)
		obj.completed = True
		obj.save()
	context = {
		'all_of_them': Item.objects.filter(user=request.user)
	}
	return render(request, 'todos.html', context)


@login_required
def new_todo(request):

	form = TodoItemForm()
	if request.method == 'POST':
		form = TodoItemForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()

	context = {
		'form': form,
	}
	return render(request, 'new_todo.html', context)