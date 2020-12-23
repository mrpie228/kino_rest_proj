from django.db import models
from django_filters import filters
from rest_framework import generics
from rest_framework.response import Response
from django.http import Http404
from django.db.models import Avg
from .serializers import (MovieAllSerializer, 
                        MovieOneDetailSerializer,
                        CreateRatingSerializer,
                        CreateReviewSerializer,
                        AllActorSerializer,
                        ActorDetailSerializer)
from .models import Actor, Movie
from django_filters.rest_framework import DjangoFilterBackend
from .utils import MovieFilter,CharFilterInFilter

class  MovieAllView(generics.ListAPIView):
    """Все фильмы"""
    serializer_class= MovieAllSerializer

    # фильтры
    filter_backends =(DjangoFilterBackend,)
    filter_class= MovieFilter
    

    #доп инфа по фильму
    def get_queryset(self):
        
        if self.request.user.is_authenticated:
            now_user=self.request.user
        else:
            now_user=None

        movies =Movie.objects.filter(draft=False
        ).annotate(that_user_rating= models.Sum('movie__star',filter=models.Q(movie__user=now_user))
        ).annotate(middle_rating=(Avg("movie__star")))
                
                
        serializer = MovieAllSerializer(movies, many = True)
        return movies


class AllActorView(generics.ListAPIView):
    """Полное описание одного актёра"""
    queryset = Actor.objects.all()
    serializer_class=AllActorSerializer

class ActorDetailView(generics.RetrieveAPIView):

    queryset = Actor.objects.all()
    serializer_class=ActorDetailSerializer


class  MovieOneDetailView(generics.RetrieveAPIView):
    """Полное описание одного фильма"""
    def get(self, request,name):
        
        try:
            movie =Movie.objects.get(url = name, draft=False)
            serializer = MovieOneDetailSerializer(movie)
        except:
            raise Http404("Что-то явно пошло не так")

        return Response(serializer.data)



class CreateReviewView(generics.CreateAPIView):
    """Выводит отзывы"""

    serializer_class= CreateReviewSerializer

class CreateRatingView(generics.CreateAPIView):
    """Для выставления рейтинга"""
    def get_user(self, request):
        user= request.user
        if user =="AnonymousUser":
            return "noname in CreateRaringView"
        return user

    serializer_class = CreateRatingSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.get_user(self.request))
