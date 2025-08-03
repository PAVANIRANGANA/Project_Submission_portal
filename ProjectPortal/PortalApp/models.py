from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import os

def validate_file_type(value):
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in ['.pdf', '.ppt', '.pptx']:
        raise ValidationError('Only PDF and PPT/PPTX files are allowed.')

class Project(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    technology_used = models.CharField(max_length=255)
    file = models.FileField(upload_to='projects/', validators=[validate_file_type])
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    status_choices = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
