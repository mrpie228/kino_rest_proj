# Generated by Django 3.1.4 on 2020-12-20 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_auto_20201220_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='ip',
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.OneToOneField(default=12, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Фильм'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='star',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.ratingstar', verbose_name='Звезда'),
        ),
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.movie', verbose_name='фильм'),
        ),
        migrations.AlterField(
            model_name='review',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='movies.review', verbose_name='Отзыв, к которому обращаются'),
        ),
    ]