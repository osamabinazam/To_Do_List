from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin


# reverse_lazy function is used to generate URL based on the name of the view function or URL Pattern
# It return a lazy object, which means that URL will not be resolved untill it is actually needed
# Useful in situations where URL might not be needed immediately
from django.urls import reverse_lazy
from todolist.models import Task

# Create your views here.

# Classed base view 
class TaskList(LoginRequiredMixin,ListView):
    # Make Task Model availabe to template for rendering and other purpose
    model = Task
    #  Help to change the object name that sent to html document
    context_object_name = 'tasks'

    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            # Filtering task for each users
            context["tasks"] = context["tasks"].filter (user=self.request.user)
            context["count"] = context["tasks"].filter(complete = False).count()

            search_input = self.request.GET.get('search-area') or ''
            if search_input:
                context['tasks'] = context['tasks'].filter (title__icontains = search_input)
                context['search_input'] =  search_input
            return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name ="tasks"
    template_name = 'todolist/task.html'        # Set custom name of the template

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task

    # field is used to display all field of the form on webpage
    # fields = "__all__"    
    # 
    # particular fields can be select
    fields = ['title', 'description', 'complete']
    success_url =  reverse_lazy("task")

    # Checking the validaity of the user before adding task
    def form_valid(self, form):
        form.instance.user  = self.request.user
        return super (TaskCreate , self).form_valid(form)
    
class TaskUpdate (LoginRequiredMixin,UpdateView):
    model = Task
    # fields = '__all__'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name ='task'
    success_url = reverse_lazy('task')

class CustomLoginView(LoginView):
    template_name = 'todolist/login.html'   # Changing template name
    fields = '__all__'                     # Using all fields
    # success_url = reverse_lazy('task')

    def get_success_url(self):
       return reverse_lazy('task')
    
class RegisterUser(FormView):
    template_name = 'todolist/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task')

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        
        return super(RegisterUser , self).form_valid(form=form)
    

    # Restricting User to access create user form when he/she is already loged in
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated :
            return redirect('task')
        
        return super(RegisterUser, self).get(*args, **kwargs)