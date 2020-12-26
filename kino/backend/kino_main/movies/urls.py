from django.urls import path

from . import views

urlpatterns = [
    path("movie/", views.MovieAllView.as_view()),
    path("movie/<name>/", views.MovieOneDetailView.as_view()),

    path("review/", views.CreateReviewView.as_view()),

    path("rate/", views.CreateRatingView.as_view()),

    path("actors/", views.AllActorView.as_view()),
    path("actors/<pk>", views.ActorDetailView.as_view()),
]
