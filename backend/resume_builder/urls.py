from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('web.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('resumes.urls')),
]
