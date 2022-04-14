from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('update_task/<str:id>/', views.updateTask, name='update-task'),
    path('delete_task/<str:id>/', views.deleteTask, name='delete-task')

    
]