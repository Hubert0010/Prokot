from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm



# Create your views here.

def dashboard(request):
    return render(request, 'registration/dashboard.html', ())

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'registration/sign_in.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'registration/sign_in.html')
def sign_up(request):
    return render (request, 'registration/register.html', ())

def logout(request):
    return render (request, 'registration/login.html', ())

