from django.shortcuts import render

def index(request):
    return render(request, 'web/index.html')

def login_view(request):
    return render(request, 'web/login.html')

def register(request):
    return render(request, 'web/register.html')

def editor(request):
    return render(request, 'web/editor.html')

def preview(request):
    return render(request, 'web/preview.html') 