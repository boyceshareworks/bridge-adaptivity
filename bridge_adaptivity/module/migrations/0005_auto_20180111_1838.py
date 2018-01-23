# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-11 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0004_auto_20180109_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engine',
            name='name',
        ),
        migrations.AddField(
            model_name='engine',
            name='engine',
            field=models.CharField(choices=[(b'engine_mock.py', b'mock'), (b'engine_vpal.py', b'vpal')], default=b'engine_mock', max_length=100),
        ),
        migrations.AddField(
            model_name='engine',
            name='engine_name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='engine',
            name='is_default',
            field=models.BooleanField(default=False, help_text='If checked Engine will be used as the default!'),
        ),
        migrations.AlterField(
            model_name='collectiongroup',
            name='collections',
            field=models.ManyToManyField(related_name='collection_groups', to='module.Collection'),
        ),
    ]
