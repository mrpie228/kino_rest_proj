# Generated by Django 3.1.4 on 2020-12-20 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='fess_in_world',
            new_name='fees_in_world',
        ),
    ]
