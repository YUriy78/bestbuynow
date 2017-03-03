# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0022_remove_ad_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'ad')),
                ('ad', models.ForeignKey(to='board.Ad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
