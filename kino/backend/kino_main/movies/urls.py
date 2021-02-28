from django.urls import path, re_path

from . import views

urlpatterns = [
    #movies
    re_path(r"^movie\/?$", views.MovieAllView.as_view()),
    path("movie/<name>/", views.MovieOneDetailView.as_view()),

    #movie rating
    re_path(r"^review\/?$", views.CreateReviewView.as_view()),
    re_path(r"^rate\/?$", views.CreateRatingView.as_view()),

    #actors
    path("actors/", views.AllActorView.as_view()),
    path("actors/<pk>", views.ActorDetailView.as_view()),

    #categories
    path("category/", views.ShowCategory.as_view()),
    path("categories/", views.ShowAllCategory.as_view()),
    path("categories/<category>/", views.ShowOneCategoryMovies.as_view()),
]
