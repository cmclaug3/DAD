from django import forms
from schedule.models import Schedule

from django.contrib.auth.forms import AuthenticationForm


class ScheduleForm(forms.ModelForm):
	class Meta:
		model = Schedule
		fields = [
			'first_name','last_name','years_playing',
			'email','introduction',
		]


class LoginForm(AuthenticationForm):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)