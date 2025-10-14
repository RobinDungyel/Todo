from . import web_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, TodoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# API routes
router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todos')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]

# Web UI routes
urlpatterns += [
    path('', web_views.home, name='home'),
    path('web/register/', web_views.register_view, name='register_web'),
    path('web/login/', web_views.login_view, name='login_web'),
    path('web/logout/', web_views.logout_view, name='logout_web'),
    path('web/todos/', web_views.todo_list_view, name='todo_list_view'),
    path('web/todos/create/', web_views.add_todo_view, name='todo_create'),
    path('web/todos/<int:pk>/edit/', web_views.edit_todo_view, name='todo_update'),
    path('web/todos/<int:pk>/delete/', web_views.delete_todo_view, name='todo_delete'),
]
