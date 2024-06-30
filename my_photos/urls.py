from django.urls import path
from . import views

urlpatterns = [
    # Ruta raíz renderizando la vista de login directamente
    path('', views.login_view, name='index'),

    # Otras rutas de tu aplicación
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
]
