# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0025_photoad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoad',
            name='ad',
        ),
        migrations.DeleteModel(
            name='PhotoAd',
        ),
    ]
