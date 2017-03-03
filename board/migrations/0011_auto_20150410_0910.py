# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_typead'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbe\xd0\xb1\xd1\x8a\xd1\x8f\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
                ('description', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbe\xd0\xb1\xd1\x8a\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
                ('price', models.DecimalField(null=True, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0', max_digits=50, decimal_places=2, blank=True)),
                ('salary', models.DecimalField(null=True, verbose_name=b'\xd0\x97\xd0\xb0\xd1\x80\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb0', max_digits=50, decimal_places=2, blank=True)),
                ('date', models.DateField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8 \xd0\xbe\xd0\xb1\xd1\x8a\xd1\x8f\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('category', models.ForeignKey(to='board.Category')),
            ],
            options={
                'verbose_name': '\u041e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u041e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81 \xd0\xbe\xd0\xb1\xd1\x8a\xd1\x8f\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u0443\u0441 \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0439',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0443\u0441\u044b \u043e\u0431\u044a\u044f\u0432\u043b\u0435\u043d\u0438\u0439',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ad',
            name='status',
            field=models.ForeignKey(to='board.Status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ad',
            name='type',
            field=models.ForeignKey(to='board.TypeAd'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ad',
            name='user',
            field=models.ForeignKey(to='board.User'),
            preserve_default=True,
        ),
    ]
