from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES

class RecordsForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Имя автора')
    email = forms.EmailField(label='E-Mail автора', required=True, widget = widgets.EmailInput)
    record = forms.CharField(max_length=2000,label='Текст', required=True, widget = widgets.Textarea)

class RecordsSearch(forms.Form):
    searched_value = forms.CharField(max_length=200, required=True, label='Поиск ')

