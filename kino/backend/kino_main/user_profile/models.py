from django.db import models
from movies.models import User,Rating,Movie 
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="Пользователь")
    photo = models.ImageField("Изображение", upload_to="profiles/photos", null=True,default="profiles/photos/no-image-user.png")
    rating = models.ManyToManyField(Rating,verbose_name="Оценки",related_name='rating', null=True)
    wath_later = models.ManyToManyField(Movie,verbose_name="Фильмы в смотреть позже",related_name='watch_later', null=True)
    liked = models.ManyToManyField(Movie,verbose_name="Понравивщиеся",related_name='liked', null=True)

    class Meta:
        verbose_name= "Профиль"
        verbose_name= "Профили"

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)