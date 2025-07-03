from rest_framework import serializers
from .models import Resume, Template


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ['id', 'name', 'template_file']


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = [
            'id', 'user', 'template', 'personal_info', 'education', 'skills',
            'summary', 'work_experience', 'projects', 'certifications', 'awards',
            'volunteering', 'languages', 'publications', 'interests', 'references',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['user', 'created_at', 'updated_at']

    def validate_education(self, value):
        for edu in value:
            for field in ['degree', 'field', 'institution', 'start_date', 'end_date']:
                if not edu.get(field):
                    raise serializers.ValidationError(f"Education: '{field}' is required.")
        return value

    def validate_work_experience(self, value):
        for job in value:
            for field in ['title', 'company', 'start_date', 'end_date']:
                if not job.get(field):
                    raise serializers.ValidationError(f"Work Experience: '{field}' is required.")
        return value

    def validate_certifications(self, value):
        for cert in value:
            for field in ['name', 'issuer', 'date']:
                if not cert.get(field):
                    raise serializers.ValidationError(f"Certification: '{field}' is required.")
        return value

    def validate_awards(self, value):
        for award in value:
            for field in ['title', 'organization', 'year']:
                if not award.get(field):
                    raise serializers.ValidationError(f"Award: '{field}' is required.")
        return value

    def validate_volunteering(self, value):
        for vol in value:
            for field in ['role', 'organization', 'dates']:
                if not vol.get(field):
                    raise serializers.ValidationError(f"Volunteering: '{field}' is required.")
        return value

    def validate_publications(self, value):
        for pub in value:
            for field in ['title', 'journal', 'date']:
                if not pub.get(field):
                    raise serializers.ValidationError(f"Publication: '{field}' is required.")
        return value

    def validate_template(self, value):
        if not value:
            raise serializers.ValidationError('A template must be selected.')
        return value 