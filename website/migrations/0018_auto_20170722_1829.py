# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-22 18:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_conversation_conv_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='last_conversation',
            field=models.DateTimeField(default=datetime.datetime(1997, 3, 30, 0, 0)),
        ),
    ]