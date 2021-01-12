
from django.db import models
from django_filters import rest_framework as filters
from .models import Category, Movie


class CharFilterInFilter(filters.BaseInFilter,filters.CharFilter):
    pass
class MovieFilter(filters.FilterSet):
    genres= CharFilterInFilter(field_name='genres__name',lookup_expr='in')
    year= filters.RangeFilter()
    movie__star=CharFilterInFilter(field_name='movie__star',lookup_expr='in')
    category= CharFilterInFilter(field_name='category__url',lookup_expr='in')

    class Meta:
        model=Movie
        fields=['genres','year','movie__star','category']