
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

from app.models import Task
from app.forms import TaskModelForm


class StartPage(TemplateView):
    template_name = 'app/start.html'


class TaskPage(ListView):
    model = Task
    template_name = 'app/tasks.html'
    context_object_name = 'tasks'
    allow_empty = False


class TaskDetail(DetailView):
    model = Task
    template_name = 'app/task_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_param'
    context_object_name = 'task'


class TaskUpdate(UpdateView):
    model = Task
    template_name = 'app/task_update.html'
    form_class = TaskModelForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug_param'
    success_url = reverse_lazy('task')
