from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer
from .models import QuizUser


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = QuizUser.objects.all()
    serializer_class = UserSerializer


