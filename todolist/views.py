from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# reverse_lazy function is used to generate URL based on the name of the view function or URL Pattern
# It return a lazy object, which means that URL will not be resolved untill it is actually needed
# Useful in situations where URL might not be needed immediately
from django.urls import reverse_lazy
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
    template_name = 'todolist/task.html'        # Set custom name of the template

class TaskCreate(CreateView):
    model = Task

    # field is used to display all field of the form on webpage
    fields = "__all__"    
    # 
    # particular fields can be select
    # fields = ['title', 'description']
    success_url =  reverse_lazy("task")
    
class TaskUpdate (UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task')

class TaskDelete(DeleteView):
    model = Task
    context_object_name ='task'
    success_url = reverse_lazy('task')