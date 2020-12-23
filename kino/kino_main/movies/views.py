from django.db import models
from django.db.models.base import Model
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from .serializers import MovieAllSerializer, MovieOneDetailSerializer,CreateRatingSerializer,CreateReviewSerializer
from .models import Movie



class  MovieAllView(APIView):

    def get(self, request):
        
        if request.user.is_authenticated:
            now_user=request.user
        else:
            now_user=None

        movies =Movie.objects.filter(draft=False
        ).annotate(user_rating= models.Sum('movie__star',filter=models.Q(movie__user=now_user))
        ).annotate(middle_rating= models.Sum(models.F('movie__star')) / models.Count('movie'))
                
                
        serializer = MovieAllSerializer(movies, many = True)
        return Response(serializer.data)





class  MovieOneDetailView(APIView):
    def get(self, request,name):
        try:
            movie =Movie.objects.get(url = name, draft=False)
            serializer = MovieOneDetailSerializer(movie)
        except:
            raise Http404("Что-то явно пошло не так")

        return Response(serializer.data)



class CreateReviewView(APIView):
    """docstring forCreateReviewView."""

    def post(self, request):
        review = CreateReviewSerializer(data= request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)

class CreateRatingView(APIView):
    
    def get_user(self, request):
        user= request.user
        if user =="AnonymousUser":
            return "noname in CreateRaringView"
        return user

    def post(self, request):

        serializer = CreateRatingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=self.get_user(request))
            return Response(status=201)
        else:
            return Response(status=400)
            #{"star":4,"movie":2}
