from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('todo', views.todo, name="todo"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('update_todo/<str:pk>/', views.updateTodo, name='update_todo' )
]
