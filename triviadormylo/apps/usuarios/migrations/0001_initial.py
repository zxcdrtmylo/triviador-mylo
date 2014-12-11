# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import triviadormylo.apps.usuarios.thumbs


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pais', models.CharField(max_length=b'30')),
                ('ciudad', models.CharField(max_length=b'30')),
                ('pasatiempo', models.CharField(max_length=b'50')),
                ('color', models.CharField(max_length=b'30')),
                ('mascota', models.CharField(max_length=b'30')),
                ('avatar', triviadormylo.apps.usuarios.thumbs.ImageWithThumbsField(upload_to=b'img_user')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
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
    ]
