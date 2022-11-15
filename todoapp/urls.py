
from django.urls import path 



from . import views

urlpatterns = [
    path("", views.todos , name="todos"),
    path("tasks", views.tasks , name="tasks"),
    path("delete/<td>/", views.deleteTask, name="delete_task"),
    path("<int:upid>", views.updatetask, name="update_task")
    
]