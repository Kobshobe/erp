# Generated by Django 2.2.4 on 2019-08-17 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_auto_20190817_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_category', models.ForeignKey(on_delete=None, to='group.LineCategory')),
            ],
        ),
    ]
