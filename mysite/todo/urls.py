from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('todo', views.todo, name="todo"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutPage, name="logout"),
    path('signup', views.signupPage, name="signup"),
    path('update_todo/<str:pk>/', views.updateTodo, name='update_todo' ),
    path('delete_todo/<str:pk>/', views.deleteTodo, name='delete_todo' )
]
