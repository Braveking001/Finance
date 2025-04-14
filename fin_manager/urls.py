# filepath: c:\Users\Olisa Olugbenga\Desktop\week14 5\FinanceManager\fin_manager\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('expenses/', name='expenses', view=views.ExpenseListView.as_view()),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]