# Generated by Django 2.2.4 on 2019-08-18 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0007_auto_20190818_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseline',
            name='status',
            field=models.CharField(choices=[('active', '启用'), ('forbidden', '禁用')], default='active', max_length=20),
        ),
    ]
