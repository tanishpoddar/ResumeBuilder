from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Template(models.Model):
    name = models.CharField(max_length=100)
    template_file = models.CharField(
        max_length=100,
        help_text='Django template filename, e.g. resume_templates/template1.html',
        blank=True,
        default=''
    )

    def __str__(self):
        return self.name

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True, blank=True)
    personal_info = models.JSONField(default=dict)
    education = models.JSONField(default=list, help_text='[{degree, field, institution, start_date: "Month Year", end_date: "Month Year", gpa}]')
    skills = models.JSONField(default=list)
    summary = models.TextField(blank=True, default='')
    work_experience = models.JSONField(default=list, help_text='[{title, company, location, start_date: "Month Year", end_date: "Month Year", responsibilities: [str]}]')
    projects = models.JSONField(default=list)
    certifications = models.JSONField(default=list, help_text='[{name, issuer, date: "Month Year"}]')
    awards = models.JSONField(default=list, help_text='[{title, organization, year, description}]')
    volunteering = models.JSONField(default=list, help_text='[{role, organization, dates: "Month Year - Month Year", description}]')
    languages = models.JSONField(default=list)
    publications = models.JSONField(default=list, help_text='[{title, journal, date: "Month Year", link}]')
    interests = models.JSONField(default=list)
    references = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Resume of {self.user.username} ({self.id})"

# NOTE: After this change, you must run makemigrations and migrate.
