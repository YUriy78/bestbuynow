# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0019_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='category',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='status',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='user',
        ),
        migrations.DeleteModel(
            name='Ad',
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0443', 'verbose_name_plural': '\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0443'},
        ),
    ]
