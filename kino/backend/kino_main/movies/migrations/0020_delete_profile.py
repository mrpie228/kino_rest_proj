# Generated by Django 3.1.4 on 2021-01-16 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0019_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]