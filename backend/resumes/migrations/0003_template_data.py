from django.db import migrations

def create_templates(apps, schema_editor):
    Template = apps.get_model('resumes', 'Template')
    templates = [
        {'name': 'Classic (Professional)', 'template_file': 'resume_templates/template1.html'},
        {'name': 'Modern (Minimalist)', 'template_file': 'resume_templates/template2.html'},
        {'name': 'Elegant (Sidebar)', 'template_file': 'resume_templates/template3.html'},
        {'name': 'Creative (Colorful)', 'template_file': 'resume_templates/template4.html'},
        {'name': 'Technical (Monochrome)', 'template_file': 'resume_templates/template5.html'},
        {'name': 'Compact (Timeline)', 'template_file': 'resume_templates/template6.html'},
    ]
    for t in templates:
        Template.objects.update_or_create(template_file=t['template_file'], defaults={'name': t['name']})

def reverse_func(apps, schema_editor):
    Template = apps.get_model('resumes', 'Template')
    files = [
        'resume_templates/template1.html',
        'resume_templates/template2.html',
        'resume_templates/template3.html',
        'resume_templates/template4.html',
        'resume_templates/template5.html',
        'resume_templates/template6.html',
    ]
    Template.objects.filter(template_file__in=files).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('resumes', '0002_remove_template_preview_image_template_template_file'),
    ]
    operations = [
        migrations.RunPython(create_templates, reverse_func),
    ] 