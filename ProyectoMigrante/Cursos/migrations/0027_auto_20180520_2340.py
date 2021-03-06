# Generated by Django 2.0.4 on 2018-05-21 06:40

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Cursos', '0026_contenidotema_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contenidotema',
            name='titulo',
        ),
        migrations.AddField(
            model_name='tema',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='tema',
            name='texto',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='tema',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=''),
        ),
        migrations.AlterField(
            model_name='preguntas',
            name='cuerpo',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='preguntas',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cursos.Course'),
        ),
        migrations.AlterField(
            model_name='preguntas',
            name='respuesta',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='preguntas',
            name='titulo',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.DeleteModel(
            name='ContenidoTema',
        ),
    ]
