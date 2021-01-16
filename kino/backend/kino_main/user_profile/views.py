from django.shortcuts import render
from rest_framework import generics
from .models import (Profile)
# Create your views here.
from .serializers import (UserProfileSerializer)


class UserProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class=UserProfileSerializer