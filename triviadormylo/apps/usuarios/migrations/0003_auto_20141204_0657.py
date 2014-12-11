# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0002_auto_20141204_0545'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contenido', models.TextField()),
                ('fecha', models.DateField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='preguntas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='respuesta',
            old_name='respuesta_opciona2',
            new_name='respusta_opciona2',
        ),
        migrations.RenameField(
            model_name='respuesta',
            old_name='respuesta_opciona3',
            new_name='respusta_opciona3',
        ),
        migrations.RenameField(
            model_name='respuesta',
            old_name='respuesta_opciona4',
            new_name='respusta_opciona4',
        ),
        migrations.RenameField(
            model_name='respuesta',
            old_name='respuesta_opcional',
            new_name='respusta_opcional',
        ),
    ]
