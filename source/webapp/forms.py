from django import forms
from django.forms import widgets
from webapp.models import status_choices


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.Form):
    description = forms.CharField(max_length=300, required=True, label = 'Описание')
    status = forms.ChoiceField(choices=status_choices, required=True, label='Статус')
    text = forms.CharField(max_length=3000, required=False, label='Подробно', widget=widgets.Textarea)
    completed_at = forms.DateField(required=False, label='Время завершения',
                                   widget=DateInput)
