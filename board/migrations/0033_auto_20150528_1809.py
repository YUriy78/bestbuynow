# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0032_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='category',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
