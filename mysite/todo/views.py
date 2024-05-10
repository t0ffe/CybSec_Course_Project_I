from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url='index')
def todo(request):
    todos = Todo.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    
    return render(request, 'todos.html', {'todos':todos, 'form':form})

@login_required(login_url='index')
def updateTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo')

    return render(request, 'update_todo.html', {'form': form})

@login_required(login_url='index')
def deleteTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todo')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')    

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(user)
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('index') 
    

def signupPage(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'signup.html', {'form': form})