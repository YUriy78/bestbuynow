# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0016_ad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xbe\xd1\x80\xd0\xb8\xd1\x82\xd0\xb5\xd1\x82 \xd0\xbe\xd0\xb1\xd1\x8a\xd1\x8f\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442 \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0439',
                'verbose_name_plural': '\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442\u044b \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0439',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='ad',
            name='category',
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
    ]
