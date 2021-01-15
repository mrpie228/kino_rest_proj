from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings



class Category(models.Model):
    """Модель категорий"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    poster = models.ImageField("Обложка жанра",null=True, upload_to="category/")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):

    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to=" rs/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"


class Genre(models.Model):

    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    #poster = models.ImageField("Обложка жанра", upload_to="genres/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):

    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2020)
    country = models.CharField("Страна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    world_premiere = models.DateField("Примьера в мире", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0,
                                         help_text="указывать сумму в долларах")
    fees_in_usa = models.PositiveIntegerField(
        "Сборы в США", default=0, help_text="указывать сумму в долларах"
    )
    fees_in_world = models.PositiveIntegerField(
        "Сборы в мире", default=0, help_text="указывать сумму в долларах"
    )
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"


class MovieShots(models.Model):

    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"


class RatingStar(models.Model):

    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Пользователь",related_name='user')
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Звезда",related_name="star")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм",related_name="movie")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        #unique_together = ['user','movie','star']
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Отзыв, к которому обращаются", on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="Пользователь")
    photo = models.ImageField("Изображение", upload_to="profiles/photos")
    rating = models.ManyToManyField(Rating,verbose_name="Оценки",related_name='rating')
    wath_later = models.ManyToManyField(Movie,verbose_name="Фильмы в смотреть позже",related_name='watch_later')
    liked = models.ManyToManyField(Movie,verbose_name="Понравивщиеся",related_name='liked')

    class Meta:
        verbose_name= "Профиль"
        verbose_name= "Профили"

#@receiver(post_save, sender=User)
#def create_user_as_customer(sender, instance, created, **kwargs):
#    if created:
#        Customer.objects.create(user=instance,name=instance.username,email=instance.email)