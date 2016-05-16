# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('card_number', models.IntegerField(unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('attempts', models.IntegerField(default=0)),
                ('balance', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('amount', models.IntegerField(null=True)),
                ('operation', models.CharField(max_length=1, choices=[(b'0', b'balance'), (b'1', b'withdrawal')])),
                ('card', models.ForeignKey(related_name='operations', to=settings.AUTH_USER_MODEL, to_field=b'card_number')),
            ],
        ),
    ]
