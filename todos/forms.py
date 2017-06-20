from django import forms

from todos.models import Item

class TodoItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['title', 'text', 'priority']


class CompleteTodoItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['id', ]
		