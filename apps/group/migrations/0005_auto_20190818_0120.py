# Generated by Django 2.2.4 on 2019-08-17 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_baseline'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseline',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='baseline',
            name='status',
            field=models.CharField(choices=[('active', '启用'), ('forbidden', '禁用')], default=0, max_length=20),
            preserve_default=False,
        ),
    ]
