from django.shortcuts import render
from .models import Todo
from .serializers import Todoserializer
from rest_framework.viewsets import ModelViewSet

class Todoview(ModelViewSet):
    queryset= Todo.objects.all()
    serializer_class = Todoserializer

