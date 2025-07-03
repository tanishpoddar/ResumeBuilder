# No tests yet.

from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Resume, Template
from .serializers import ResumeSerializer
from django.urls import reverse
from unittest.mock import patch

class ResumeSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.template = Template.objects.create(name='Test Template', template_file='resume_templates/template1.html')

    def test_missing_required_education_field(self):
        data = {
            'user': self.user.id,
            'template': self.template.id,
            'personal_info': {},
            'education': [{'degree': '', 'field': 'CS', 'institution': 'X', 'start_date': 'Jan 2020', 'end_date': 'Jan 2024'}],
            'skills': [], 'summary': '', 'work_experience': [], 'projects': [], 'certifications': [], 'awards': [], 'volunteering': [], 'languages': [], 'publications': [], 'interests': [], 'references': []
        }
        serializer = ResumeSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('education', serializer.errors)

    def test_valid_resume(self):
        data = {
            'user': self.user.id,
            'template': self.template.id,
            'personal_info': {},
            'education': [{'degree': 'BSc', 'field': 'CS', 'institution': 'X', 'start_date': 'Jan 2020', 'end_date': 'Jan 2024'}],
            'skills': [], 'summary': '', 'work_experience': [], 'projects': [], 'certifications': [], 'awards': [], 'volunteering': [], 'languages': [], 'publications': [], 'interests': [], 'references': []
        }
        serializer = ResumeSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class ExportResumePDFViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.template = Template.objects.create(name='Test Template', template_file='resume_templates/template1.html')
        self.resume = Resume.objects.create(user=self.user, template=self.template, personal_info={}, education=[], skills=[], summary='', work_experience=[], projects=[], certifications=[], awards=[], volunteering=[], languages=[], publications=[], interests=[], references=[])

    @patch('resumes.views.requests.post')
    def test_export_resume_pdf_requires_auth(self, mock_post):
        url = reverse('resume-export-pdf', args=[self.resume.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    @patch('resumes.views.requests.post')
    def test_export_resume_pdf_success(self, mock_post):
        self.client.login(username='testuser', password='testpass')
        mock_post.return_value.ok = True
        mock_post.return_value.content = b'%PDF-1.4...'
        url = reverse('resume-export-pdf', args=[self.resume.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
