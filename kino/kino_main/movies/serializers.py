from rest_framework import serializers

from .models import *

class MovieAllSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    user_rating = serializers.FloatField()
    middle_rating = serializers.FloatField()
    class Meta:
         model = Movie
         fields = ('title','tagline','category','url','middle_rating','user_rating')



class RecursiveSerializer(serializers.Serializer):

    def to_representation (self,value):
        serializer = self.parent.parent.__class__(value,context=self.context)
        return serializer.data

class NoRepeatReviewSerializer(serializers.ListSerializer):

    def to_representation (self,data):
        data = data.filter (parent = None)
        return super().to_representation(data)



class CreateReviewSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
         model = Review
         fields = '__all__'

class ShowReviewSerializer(serializers.ModelSerializer):

    children = RecursiveSerializer(many=True)
    class Meta:
        list_serializer_class= NoRepeatReviewSerializer
        model = Review
        fields = ("name","text","children")


class MovieOneDetailSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = serializers.SlugRelatedField(slug_field="name", read_only=True, many= True)
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many= True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many= True)
    reviews = ShowReviewSerializer(many = True)
    class Meta:
         model = Movie
         exclude = ('draft',)


class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('movie','star')

    def new(self,validated_data):
        
        rating = Rating.objects.get_or_create(
            
        user= validated_data.get('user',None),
        movie= validated_data.get('movie',None),
        defaults={'start': validated_data.get('star')}
        )
        return rating
