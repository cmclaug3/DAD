from django import forms
from schedule.models import Lesson

from django.contrib.auth.forms import AuthenticationForm


class LessonForm(forms.ModelForm):
	class Meta:
		model = Lesson
		fields = [
			'first_name','last_name','years_playing',
			'email','tell_us_about_yourself',
		]


class LoginForm(AuthenticationForm):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)