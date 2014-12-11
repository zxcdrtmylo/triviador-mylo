# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('respuesta_correcta', models.CharField(max_length=500)),
                ('respuesta_opcional', models.CharField(max_length=500)),
                ('respuesta_opciona2', models.CharField(max_length=500)),
                ('respuesta_opciona3', models.CharField(max_length=500)),
                ('respuesta_opciona4', models.CharField(max_length=500)),
                ('pregunta', models.ForeignKey(to='usuarios.Pregunta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comentarios',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='comentarios',
        ),
        migrations.DeleteModel(
            name='preguntas',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='tema',
            field=models.ForeignKey(to='usuarios.Tema'),
            preserve_default=True,
        ),
    ]
