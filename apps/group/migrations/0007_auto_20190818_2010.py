# Generated by Django 2.2.4 on 2019-08-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0006_auto_20190818_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linecategory',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='linecategory',
            name='contract_type',
            field=models.CharField(choices=[('native', '国内游'), ('abroad', '国外游'), ('one_day', '一日游'), ('Taiwan', '台湾游')], default='native', max_length=10, verbose_name='合同类型'),
        ),
        migrations.AlterField(
            model_name='linecategory',
            name='deduction_point',
            field=models.CharField(default='0', max_length=100, verbose_name='扣点'),
        ),
        migrations.AlterField(
            model_name='linecategory',
            name='product_type',
            field=models.CharField(choices=[('native', '国内'), ('abroad', '出境'), ('surround', '周边'), ('other', '其它'), ('mail_steamer', '邮轮')], default='native', max_length=10, verbose_name='产品类型'),
        ),
        migrations.AlterField(
            model_name='linecategory',
            name='status',
            field=models.CharField(choices=[('active', '启用'), ('forbidden', '禁用')], default='active', max_length=20, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='linecategory',
            name='supplier_amount',
            field=models.IntegerField(default=0, verbose_name='供应商数量'),
        ),
        migrations.AlterField(
            model_name='linecategory',
            name='tag_info',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='标签信息'),
        ),
        migrations.AlterField(
            model_name='linecategory',
            name='type_account',
            field=models.IntegerField(default=0, verbose_name='线路数量'),
        ),
        migrations.AlterField(
            model_name='linecategory',
            name='type_name',
            field=models.CharField(max_length=100, verbose_name='类别名称'),
        ),
        migrations.AlterField(
            model_name='linecategory',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='权重'),
        ),
    ]