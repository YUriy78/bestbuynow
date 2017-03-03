# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_feedback_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeAd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xbe\xd0\xb1\xd1\x8a\xd1\x8f\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb9')),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0439',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0439',
            },
            bases=(models.Model,),
        ),
    ]
