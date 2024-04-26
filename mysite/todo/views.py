from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')


def todo(request):
    tasks = Task.objects.all()
    print(tasks)
    #, {'tasks':tasks}
    return render(request, 'todos.html')

def login(request):
    
    
    return render(request, 'login.html')