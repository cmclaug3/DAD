# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from schedule.models import Schedule
from schedule.forms import ScheduleForm

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def home(request):
	return render(request, 'home.html')

def lesson_main(request):
	form_class = ScheduleForm
	form = form_class(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
	return render(request, 'lesson_form.html', {'form': form})


def lesson_submit(request):
	form_class = ScheduleForm
	form = form_class(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		else:
			form = ScheduleForm()

	return render(request, 'lesson_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        #print('form is post')
        form = AuthenticationForm(request.POST)
        #if form.is_valid():
        print('form is valid')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            print('user could not login')
        #else:
            #print('form not valid')
            #import ipdb
            #ipdb.set_trace()
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
        'msg': 'you are already logged in',
        'msg2': 'incorrect credentials',
    }
    return render(request, 'login.html', context)


