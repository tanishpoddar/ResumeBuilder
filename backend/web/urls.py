from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
    path('editor/', views.editor, name='editor'),
    path('preview/', views.preview, name='preview'),
]
