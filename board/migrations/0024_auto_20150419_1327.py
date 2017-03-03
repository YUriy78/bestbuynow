# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0023_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='ad',
        ),
        migrations.DeleteModel(
            name='Photos',
        ),
    ]
