from django import forms 
from .models import TodoItem

class Todoform(forms.ModelForm):

	class Meta:
		model = TodoItem
		fields=('title_text','notes')

