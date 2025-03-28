from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notes,NotesSerializers

@api_view(['GET'])
def notes(request):
    notes=Notes.objects.all()
    serializer=NotesSerializers(notes,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def notessec(request,sec):
    notes=Notes.objects.filter(section=sec)
    print()
    serializer=NotesSerializers(notes,many=True)
    return Response(serializer.data)
