# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from schedule.models import Lesson
from schedule.forms import LessonForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(request, 'home.html')

def lesson_main(request):
    form_class = LessonForm
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
    msg2 = ''
    if request.user.is_authenticated:
        msg2 = 'you are already logged in'
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
            msg2 = 'incorrect credentials'
        #else:
            #print('form not valid')
            #import ipdb
            #ipdb.set_trace()
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
        'msg': msg2,
    }
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')



