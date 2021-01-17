
from rest_framework import serializers

from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    
    class Meta:
         model = Profile
         fields = ("user","watch_later","liked")

