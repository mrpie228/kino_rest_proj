
from django.db.models import fields
from rest_framework import serializers

from .models import *


class WatchLaterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ("title","url")

class LikedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ("title","url")


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    watch_later = WatchLaterSerializer(read_only=True, many=True)
    liked = LikedSerializer(read_only=True, many=True)
    
    class Meta:
         model = Profile
         fields = ("user","watch_later","liked")
