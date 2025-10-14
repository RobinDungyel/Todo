from django.urls import path
from . import web_views

urlpatterns = [
    path('', web_views.home, name='home'),
    path('register/', web_views.register_view, name='register'),
    path('login/', web_views.login_view, name='login'),
    path('logout/', web_views.logout_view, name='logout'),
    path('todos/', web_views.todo_list_view, name='todo_list'),
    path('todos/add/', web_views.add_todo_view, name='add_todo'),
    path('todos/edit/<int:pk>/', web_views.edit_todo_view, name='edit_todo'),
    path('todos/delete/<int:pk>/', web_views.delete_todo_view, name='delete_todo'),
]
