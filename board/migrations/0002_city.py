# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4')),
            ],
            options={
                'verbose_name': '\u0413\u043e\u0440\u043e\u0434',
                'verbose_name_plural': '\u0413\u043e\u0440\u043e\u0434\u0430',
            },
            bases=(models.Model,),
        ),
    ]
