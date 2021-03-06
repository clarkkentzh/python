# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='static/default.png', max_length=200, null=True, upload_to='avatar/%Y/%m', verbose_name='Head_portrait')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='static/default.png', max_length=200, null=True, upload_to='avatar/%Y/%m', verbose_name='Head_portrait'),
        ),
    ]
