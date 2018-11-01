# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-01 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=64)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
