from django.shortcuts import render

from rest_framework import generics

from application1.models import Application
from .serializers import ApplicationSerializer

class ApplicationAPIView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
