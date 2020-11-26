# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-08 21:43
from __future__ import unicode_literals

from oidc_provider import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.get("OIDC_USER_MODEL")),
        ('oidc_provider', '0022_auto_20170331_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='oidc_clients_set', to=settings.get("OIDC_USER_MODEL"), verbose_name='Owner'),
        ),
    ]
