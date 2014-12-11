# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20141211_0200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sala',
            old_name='nombre',
            new_name='nom_sala',
        ),
    ]
