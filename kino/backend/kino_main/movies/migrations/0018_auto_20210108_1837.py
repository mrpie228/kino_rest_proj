# Generated by Django 3.1.4 on 2021-01-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0017_auto_20201223_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='poster',
            field=models.ImageField(null=True, upload_to='category/', verbose_name='Обложка жанра'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(default=2020, verbose_name='Дата выхода'),
        ),
    ]
