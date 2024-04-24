from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    print(tasks)
    #, {'tasks':tasks}
    return render(request, 'index.html')