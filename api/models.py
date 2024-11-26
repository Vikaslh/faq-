from django.db import models

# Create your models here.
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    uploaded_by = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)

class FAQ(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='faqs')
    question = models.TextField()
    answer = models.TextField()
    generated_date = models.DateTimeField(auto_now_add=True)

from django.db import models

class UploadedDocument(models.Model):
    document = models.FileField(upload_to='documents/')  # Store in 'documents' folder
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document uploaded at {self.uploaded_at}"
