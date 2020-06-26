from django import forms
from . import models


class CreateList(forms.ModelForm):
    class Meta:
        model = models.Todolist
        fields = ['text']
