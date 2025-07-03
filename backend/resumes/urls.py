from django.urls import path
from .views import (
    TemplateListView, TemplateDetailView,
    ResumeListCreateView, ResumeDetailView,
    RegisterView, CustomObtainAuthToken,
    export_resume_pdf, render_resume_html
)

urlpatterns = [
    path('templates/', TemplateListView.as_view(), name='template-list'),
    path('templates/<int:pk>/', TemplateDetailView.as_view(), name='template-detail'),
    path('resumes/', ResumeListCreateView.as_view(), name='resume-list-create'),
    path('resumes/<int:pk>/', ResumeDetailView.as_view(), name='resume-detail'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', CustomObtainAuthToken.as_view(), name='login'),
    path('resumes/<int:pk>/export_pdf/', export_resume_pdf, name='resume-export-pdf'),
    path('resumes/<int:pk>/render/', render_resume_html, name='render-resume-html'),
] 