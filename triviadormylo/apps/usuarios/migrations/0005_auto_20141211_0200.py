# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_sala'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respuesta',
            old_name='respusta_opciona2',
            new_name='respuesta_incorec1',
        ),
        migrations.RenameField(
            model_name='respuesta',
            old_name='respusta_opciona3',
            new_name='respuesta_incorec2',
        ),
        migrations.RenameField(
            model_name='respuesta',
            old_name='respusta_opciona4',
            new_name='respuesta_incorec3',
        ),
        migrations.RenameField(
            model_name='respuesta',
            old_name='respusta_opcional',
            new_name='respuesta_incorec4',
        ),
    ]
