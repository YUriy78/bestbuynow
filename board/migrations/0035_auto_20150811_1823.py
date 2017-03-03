# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0034_auto_20150528_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='IconMainCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.FileField(upload_to=b'icon', verbose_name=b'\xd0\x98\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0', blank=True)),
                ('main_category', models.ForeignKey(to='board.MainCategory')),
            ],
            options={
                'verbose_name': '\u0418\u043a\u043e\u043d\u043a\u0430',
                'verbose_name_plural': '\u0418\u043a\u043e\u043d\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4'),
        ),
        migrations.AlterField(
            model_name='maincategory',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name=b'\xd0\x93\xd0\xbb\xd0\xb0\xd0\xb2\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f'),
        ),
    ]
