# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 14:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Policy', to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL)),
            ],
        ),
    ]
