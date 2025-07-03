from rest_framework import generics, permissions
from .models import Resume, Template
from .serializers import ResumeSerializer, TemplateSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import os

# Create your views here.

class TemplateListView(generics.ListAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = [permissions.AllowAny]

class TemplateDetailView(generics.RetrieveAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = [permissions.AllowAny]

class ResumeListCreateView(generics.ListCreateAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ResumeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if not username or not password:
            return Response({'error': 'Username and password required.'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password, email=email)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username, 'email': user.email}, status=status.HTTP_201_CREATED)

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'username': token.user.username, 'email': token.user.email})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def export_resume_pdf(request, pk):
    try:
        resume = Resume.objects.get(pk=pk, user=request.user)
    except Resume.DoesNotExist:
        raise Http404('Resume not found')
    template_file = resume.template.template_file
    if not template_file:
        return HttpResponse('No template assigned.', status=400)
    
    # Render the template content normally
    html = render_to_string(template_file, {
        'personal_info': resume.personal_info,
        'summary': resume.summary,
        'education': resume.education,
        'work_experience': resume.work_experience,
        'projects': resume.projects,
        'skills': resume.skills,
        'certifications': resume.certifications,
        'awards': resume.awards,
        'volunteering': resume.volunteering,
        'languages': resume.languages,
        'publications': resume.publications,
        'interests': resume.interests,
        'references': resume.references,
    })
    
    # Clean the HTML for PDF - enforce white background and proper margins, remove only end borders
    html = html.replace('background: #f8f9fa', 'background: white')
    html = html.replace('box-shadow: 0 2px 8px #e0e0e0', 'box-shadow: none')
    html = html.replace('border-radius: 8px', 'border-radius: 0')
    # Remove only border-bottom from last section headings
    html = html.replace('.section:last-child h2 { border-bottom: none !important; }', '.section:last-child h2 { border-bottom: none !important; }')
    # Add pure white background to html and body
    html = html.replace('<style>', '<style>html { background: white !important; } body { background: white !important; }')
    html = html.replace('body {', 'body { background: white !important; margin: 24mm; ')
    
    # Remove any remaining card styling
    html = html.replace('max-width: 800px; margin: auto; background: #fff; box-shadow: 0 2px 8px #e0e0e0; padding: 40px; border-radius: 8px;', '')
    
    # PDFShift API integration (latest endpoint and header)
    api_key = os.environ.get('PDFSHIFT_API_KEY')
    if not api_key:
        return HttpResponse('PDFShift API key not set. Please set PDFSHIFT_API_KEY in your environment.', status=500)
    
    try:
        pdf_response = requests.post(
            'https://api.pdfshift.io/v3/convert/pdf',
            headers={'X-API-Key': api_key},
            json={
                'source': html,
                'format': 'A4'
            }
        )
        if pdf_response.ok:
            pdf = pdf_response.content
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="resume_{resume.id}.pdf"'
            return response
        else:
            return HttpResponse(f'PDF generation failed: {pdf_response.status_code} - {pdf_response.text}', status=500)
    except Exception as e:
        return HttpResponse(f'PDF generation error: {str(e)}', status=500)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def render_resume_html(request, pk):
    try:
        resume = Resume.objects.get(pk=pk, user=request.user)
    except Resume.DoesNotExist:
        raise Http404('Resume not found')
    template_file = resume.template.template_file
    if not template_file:
        return HttpResponse('No template assigned.', status=400)
    
    # Render the template content normally
    html = render_to_string(template_file, {
        'personal_info': resume.personal_info,
        'summary': resume.summary,
        'education': resume.education,
        'work_experience': resume.work_experience,
        'projects': resume.projects,
        'skills': resume.skills,
        'certifications': resume.certifications,
        'awards': resume.awards,
        'volunteering': resume.volunteering,
        'languages': resume.languages,
        'publications': resume.publications,
        'interests': resume.interests,
        'references': resume.references,
    })
    return HttpResponse(html)
