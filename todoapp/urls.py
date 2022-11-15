
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path("", views.todos , name="todos"),
    path("tasks", views.tasks , name="tasks"),
    path("delete/<td>/", views.deleteTask, name="delete_task"),
    path("<int:upid>", views.updatetask, name="update_task")
    
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIR)
