from django import forms

from app.models import Task


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline_date', 'level_task', 'status_task']