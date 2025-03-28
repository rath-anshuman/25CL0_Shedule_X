from django.db import models
from cloudinary.models import CloudinaryField


class SectionSelector(models.TextChoices):
    A ="A","A"
    B ="B","B"
    C ="C","C"

class Notes(models.Model):
    title=models.CharField(max_length=600)
    description=models.CharField(max_length=6000,null=True,blank=True)
    file = CloudinaryField('file', resource_type='auto',null=True,blank=True,folder='schedulex') 
    section=models.CharField(max_length=2,choices=SectionSelector.choices)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
from rest_framework.serializers import ModelSerializer

class NotesSerializers(ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'