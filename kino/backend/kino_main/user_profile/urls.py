from django.urls import path, re_path

from . import views

urlpatterns = [
    path("profile/<pk>", views.UserProfileView.as_view()),

]
