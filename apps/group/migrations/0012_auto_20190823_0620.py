# Generated by Django 2.2.4 on 2019-08-23 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0011_auto_20190823_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='linecategory',
            name='admID',
            field=models.IntegerField(default=15447, verbose_name='admID字段'),
        ),
        migrations.AddField(
            model_name='linecategory',
            name='erpid',
            field=models.IntegerField(default=1, verbose_name='ERP_ID'),
        ),
        migrations.AddField(
            model_name='linecategory',
            name='img',
            field=models.CharField(default='这是img字段', max_length=200, verbose_name='img字段'),
        ),
    ]
