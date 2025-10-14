from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),      # API routes
    path('', include('api.web_urls')),      # Web UI routes
    path('', RedirectView.as_view(url='/todos/')),  # Default redirect
]
