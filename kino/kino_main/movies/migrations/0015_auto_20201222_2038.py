# Generated by Django 3.1.4 on 2020-12-22 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0014_auto_20201222_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
