# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0024_auto_20150419_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoAd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(upload_to=b'ad', verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb8')),
                ('ad', models.ForeignKey(to='board.Ad')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u044f',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438 \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0439',
            },
            bases=(models.Model,),
        ),
    ]
