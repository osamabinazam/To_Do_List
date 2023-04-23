from django.urls import path 
# from . import views
from .views import TaskList, TaskDetail,TaskCreate

urlpatterns = [
    path('',TaskList.as_view(), name='task'),
    path('task/<int:pk>/' , TaskDetail.as_view(), name='task-detail') ,
    path ('task-create/' , TaskCreate.as_view(), name="task-create"),
]
