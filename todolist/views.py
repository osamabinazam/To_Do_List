from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from todolist.models import Task

# Create your views here.

# Classed base view 
class TaskList(ListView):
    # Make Task Model availabe to template for rendering and other purpose
    model = Task
    #  Help to change the object name that sent to html document
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    context_object_name ="tasks"
    template_name = 'todolist/task.html'
