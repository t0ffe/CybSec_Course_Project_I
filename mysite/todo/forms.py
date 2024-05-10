from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import * 

class TodoForm(ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'completed']


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']