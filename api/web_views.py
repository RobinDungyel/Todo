from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Todo
from .forms import RegisterForm, LoginForm, TodoForm

def home(request):
    if request.user.is_authenticated:
        return redirect('todo_list')
    return redirect('login')

def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('todo_list')
    elif request.method == 'POST' and not form.is_valid():
        messages.error(request, 'Please fix the errors below.')
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'GET' and request.user.is_authenticated:
        return redirect('todo_list')
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next') or request.POST.get('next')
            return redirect(next_url or 'todo_list')
        else:
            messages.error(request, 'Invalid username or password.')
    elif request.method == 'POST' and not form.is_valid():
        messages.error(request, 'Please enter both username and password.')
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def todo_list_view(request):
    todos = Todo.objects.filter(user=request.user)
    status_filter = request.GET.get('status')
    if status_filter == 'completed':
        todos = todos.filter(completed=True)
    elif status_filter == 'incomplete':
        todos = todos.filter(completed=False)
    # If no filter or 'all', show all todos (default behavior)  
    return render(request, 'todo_list.html', {'todos': todos, 'status_filter': status_filter})

@login_required
def add_todo_view(request):
    form = TodoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo_form.html', {'form': form})

@login_required
def edit_todo_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    form = TodoForm(request.POST or None, instance=todo)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todo_form.html', {'form': form})

@login_required
def delete_todo_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'confirm_delete.html', {'todo': todo})
