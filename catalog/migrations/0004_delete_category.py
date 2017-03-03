# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
