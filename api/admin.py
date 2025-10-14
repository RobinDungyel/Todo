from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','title','user','completed','created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'description', 'user__username')
