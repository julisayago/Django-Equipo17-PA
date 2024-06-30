from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='index'),  
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
]