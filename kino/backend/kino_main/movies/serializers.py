
from rest_framework import serializers

from .models import *

class MovieAllSerializer(serializers.ModelSerializer):
    #для вывода всех фильмов
    category = serializers.SlugRelatedField(slug_field="url", read_only=True)
    category_url = serializers.SlugRelatedField(slug_field="url", read_only=True)
    that_user_rating = serializers.FloatField()
    middle_rating = serializers.FloatField()
    class Meta:
         model = Movie
         fields = ('title',"poster",'tagline','category','category_url','url','middle_rating','that_user_rating')

class AllActorSerializer(serializers.ModelSerializer):
    #для вывода всех актёров
    class Meta:
        model = Actor
        fields= ("id","name","image")

class ActorDetailSerializer(serializers.ModelSerializer):
    #для вывода полного описания актёров
    class Meta:
        model = Actor
        fields= '__all__'



class RecursiveSerializer(serializers.Serializer):
    #для вывода дочерних отзывов
    def to_representation (self,value):
        serializer = self.parent.parent.__class__(value,context=self.context)
        return serializer.data

class NoRepeatReviewSerializer(serializers.ListSerializer):
    #для того, чтобы не репитились комментарии
    def to_representation (self,data):
        data = data.filter (parent = None)
        return super().to_representation(data)



class CreateReviewSerializer(serializers.ModelSerializer):
    #для создания отзыва
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
         model = Review
         fields = '__all__'

class ShowReviewSerializer(serializers.ModelSerializer):
    #для вывода отзывов
    children = RecursiveSerializer(many=True)
    class Meta:
        list_serializer_class= NoRepeatReviewSerializer
        model = Review
        fields = ("name","text","children")



class MovieOneDetailSerializer(serializers.ModelSerializer):
    #полное описание видео
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = AllActorSerializer(read_only=True, many= True)
    actors = AllActorSerializer(read_only=True, many= True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many= True)
    reviews = ShowReviewSerializer(many = True)
    class Meta:
         model = Movie
         exclude = ('draft',)


class CreateRatingSerializer(serializers.ModelSerializer):
    #для создания рейтинга (звездочки)
    class Meta:
        model = Rating
        fields = ('star','movie')

    def create(self,validated_data):
        
        rating,_ = Rating.objects.update_or_create(

        user= validated_data.get('user',None),
        movie= validated_data.get('movie',None),
        defaults={'star': validated_data.get("star")},
        )
        return rating



class ShowCategorySerializer(serializers.ModelSerializer):
    #для вывода категорий на гл. страницу
    class Meta:
        model = Category
        fields= ('id','name','poster','url')



class ShowAllCategorySerializer(serializers.ModelSerializer):
    #для вывода всех категорий
    class Meta:
        model = Category
        fields= ('id','name','poster','url')



class ShowOneCategoryMoviesSerializer(serializers.ModelSerializer):
   #для вывода видео из одной категории
    class Meta:
        model = Movie
        fields = "__all__"