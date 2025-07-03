from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'web/landing.html')

def about(request):
    return render(request, 'web/about.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST' and 'username' in request.POST and 'password' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'web/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST' and 'username' in request.POST and 'password' in request.POST and 'email' in request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not username or not password or not email:
            messages.error(request, 'All fields are required.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('index')
    return render(request, 'web/login.html')

def logout_view(request):
    if request.method in ['GET', 'POST']:
        logout(request)
        return redirect('landing')
    return redirect('landing')

@login_required(login_url='/login/')
def index(request):
    # This will be the dashboard/template selection page
    return render(request, 'web/index.html')

def editor(request):
    return render(request, 'web/editor.html')

def preview(request):
    return render(request, 'web/preview.html')
