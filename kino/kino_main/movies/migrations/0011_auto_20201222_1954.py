# Generated by Django 3.1.4 on 2020-12-22 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_auto_20201222_1945'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
    ]
