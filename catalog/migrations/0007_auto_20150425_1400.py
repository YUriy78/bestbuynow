# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_usercompany'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercompany',
            name='category',
        ),
        migrations.RemoveField(
            model_name='usercompany',
            name='city',
        ),
        migrations.RemoveField(
            model_name='usercompany',
            name='status',
        ),
        migrations.RemoveField(
            model_name='usercompany',
            name='user_account',
        ),
        migrations.DeleteModel(
            name='UserCompany',
        ),
    ]
