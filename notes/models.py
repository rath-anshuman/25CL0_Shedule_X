from django.db import models
from cloudinary.models import CloudinaryField


class SectionSelector(models.TextChoices):
    A ="A","A"
    B ="B","B"
    C ="C","C"

class SubjectTitles(models.TextChoices):
    FUNDAMENTALS_OF_DATA_ANALYTICS = "Fundamentals of Data Analytics", "Fundamentals of Data Analytics"
    INTRO_TO_MOBILE_COMP = "Introduction to Mobile Computation", "Introduction to Mobile Computation"
    ANDROID_DEV = "Mobile Application Development Using Android", "Mobile Application Development Using Android"
    AI = "Artificial Intelligence", "Artificial Intelligence"
    IOT = "Internet of Things", "Internet of Things"
    PROJECT = "Project", "Project"

class Notes(models.Model):
    title = models.CharField(max_length=600, choices=SubjectTitles.choices)
    description = models.CharField(max_length=6000, null=True, blank=True)
    file = CloudinaryField('file', resource_type='auto', null=True, blank=True, folder='schedulex') 
    section = models.CharField(max_length=2, choices=SectionSelector.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    
from rest_framework.serializers import ModelSerializer

class NotesSerializers(ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'