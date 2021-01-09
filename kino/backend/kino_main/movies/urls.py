from django.urls import path, re_path

from . import views

urlpatterns = [
    path("movie/", views.MovieAllView.as_view()),
    path("movie/<name>/", views.MovieOneDetailView.as_view()),

    path("review/", views.CreateReviewView.as_view()),

    re_path(r"^rate/$", views.CreateRatingView.as_view()),

    path("actors/", views.AllActorView.as_view()),
    path("actors/<pk>", views.ActorDetailView.as_view()),


    path("category/", views.ShowCategory.as_view()),
     path("categories/", views.ShowAllCategory.as_view()),
]
