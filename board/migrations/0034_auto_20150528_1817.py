# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0033_auto_20150528_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75, verbose_name=b'Email \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xbf\xd0\xb8\xd1\x81\xd1\x87\xd0\xb8\xd0\xba\xd0\xb0')),
                ('category', models.ForeignKey(to='board.Category')),
            ],
            options={
                'verbose_name': '\u041f\u043e\u0434\u043f\u0438\u0441\u043a\u0430 \u043d\u0430 \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u044f',
                'verbose_name_plural': '\u041f\u043e\u0434\u043f\u0438\u0441\u043a\u0438 \u043d\u0430 \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sign', models.CharField(max_length=5, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xb4\xd1\x82\xd0\xb2\xd0\xb5\xd1\x80\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xb4\xd0\xbf\xd0\xb8\xd1\x81\xd0\xba\xd0\xb8')),
            ],
            options={
                'verbose_name': '\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435 \u043f\u043e\u0434\u043f\u0438\u0441\u043e\u043a',
                'verbose_name_plural': '\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f \u043f\u043e\u0434\u043f\u0438\u0441\u043e\u043a',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='subscription',
            name='verification',
            field=models.ForeignKey(to='board.Verification'),
            preserve_default=True,
        ),
    ]
