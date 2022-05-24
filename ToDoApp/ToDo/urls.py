from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing, name = 'landing'),
    path('lists/',views.tasks, name = 'tasks'),
    path('update/<str:pk>/',views.update_task,name='update_task'),
    path('delete/<str:pk>/',views.delete,name='delete_task'),
    
]