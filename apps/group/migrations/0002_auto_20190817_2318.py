# Generated by Django 2.2.4 on 2019-08-17 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linecategory',
            old_name='line_amount',
            new_name='type_account',
        ),
        migrations.RemoveField(
            model_name='linecategory',
            name='en_name',
        ),
        migrations.AlterField(
            model_name='linecategory',
            name='product_type',
            field=models.CharField(max_length=200, verbose_name='英文'),
        ),
    ]