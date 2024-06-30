from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render



def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirigir a la página "Home"
        else:
            return HttpResponse("Usuario o contraseña incorrectos")
    return render(request, 'my_photos/login.html')

@login_required
def home_view(request):
    return render(request, 'my_photos/home.html')

def profile_view(request):
    return render(request, 'my_photos/profile.html')