# Generated by Django 2.0.4 on 2018-05-13 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0025_auto_20180428_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenidotema',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
