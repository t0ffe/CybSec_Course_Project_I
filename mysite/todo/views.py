from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import connection #for the unsafe db insertion

# Create your views here.
def index(request):
    #-----------------------------------------------------------
    username = request.session.get("loggedin")
    #-----------------------------------------------------------
    return render(request, 'index.html', {'username':username})

#@login_required(login_url='index')
def todo(request):
    
    #-----------------------------------------------------------
    #4. A01:2021-Broken Access Control. Anyone can say every todo.
    todos = Todo.objects.all()
    #-----------------------------------------------------------

    #4. A01:2021-Broken Access Control. Filter so that user can only see their own todos.
    #todos = Todo.objects.filter(created_by=request.user)
    form = TodoForm()

    #-----------------------------------------------------------
    #1. A03:2021-Injection. Unsafe way
    if request.method == 'POST':

        # If you give as todo's title the following:
        # 1','0','2'); DROP TABLE todo_todo; --
        # it will drop the table that has all the todos rendering the app unusable.
        
        # The following input:
        # 1','0','2'); UPDATE todo_todo SET title='hacked' WHERE 1 = 1; --
        # changes all task's titles to 'hacked'. 
        # This is a safer way to see that injection is possible, without completely destroying the app.

        cursor = connection.cursor()        
        raw_title = request.POST.get('title','')
        raw_query = "INSERT INTO todo_todo (title, completed, created_by_id) VALUES ('%s', '0', '2')" % (raw_title)
        cursor.executescript(raw_query)

        return redirect('todo')
    #-----------------------------------------------------------

    #1. A03:2021-Injection. Safe way / fix.
    #if request.method == 'POST':
    #    form = TodoForm(request.POST)
    #    todo = form.save(commit=False)
    #    todo.created_by = request.user
    #    if form.is_valid():
    #        form.save()
    #        return redirect('todo')
    
    return render(request, 'todos.html', {'todos':todos, 'form':form})

#@login_required(login_url='index')
def updateTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo')

    return render(request, 'update_todo.html', {'form': form})

#@login_required(login_url='index')
def deleteTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todo')

def loginPage(request):
    if request.method == 'POST':

        #-----------------------------------------------------------
        #2. A07:2021-Identification and Authentication Failures. Unsafe way.
        #3. A02:2021-Cryptographic Failures. Unsafe way.
        username = request.POST.get('username')
        password = request.POST.get('password')  
        user = UnsafeUser.objects.get(username=username)

        if user.password == password:
            request.session["loggedin"] = username
            return redirect('index')
        #-----------------------------------------------------------

        #2. A07:2021-Identification and Authentication Failures. Safe way / fix.
        #3. A02:2021-Cryptographic Failures. Safe way / fix.
        #user = authenticate(request, username=username, password=password)
        #if user is not None:
        #    login(request, user)
        #    return redirect('index')
        #else:
        #    return redirect('login')

    return render(request, 'login.html')

def logoutPage(request):
    #-----------------------------------------------------------
    request.session["loggedin"] = ''
    #-----------------------------------------------------------
    
    #logout(request)
    return redirect('index') 
    

def signupPage(request):
    form = SignUpForm()

    
    #-----------------------------------------------------------
    #2. A07:2021-Identification and Authentication Failures. Unsafe way.
    #3. A02:2021-Cryptographic Failures. Unsafe way.

    # This way allows the creation of users with weak passwords.
    # They are stored in UnsafeUsers.
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        print(username, password)
        UnsafeUser.objects.create(username = username, password = password)
        return redirect('login')
    #-----------------------------------------------------------

    #2. A07:2021-Identification and Authentication Failures. Safe way / fix.
    #3. A02:2021-Cryptographic Failures. Safe way / fix.
    #if request.method == 'POST':
    #    form = SignUpForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        return redirect('login')

    return render(request, 'signup.html', {'form': form})