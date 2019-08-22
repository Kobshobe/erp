from datetime import datetime

from django.db import models

# Create your models here.
# from user.models import UserProfile


class TestModel(models.Model):
    name = models.CharField(max_length=20,verbose_name='名字')
    age = models.IntegerField(verbose_name='年龄')
    add_time = models.DateTimeField(default=datetime.now)


class LineCategory(models.Model):
    """线路类别"""
    #状态
    isLockItems = (('active', '启用'), ('forbidden', '禁用'))
    #线路类别
    lineTypeItems = (('native', '国内'), ('abroad', '出境'), ('surround', '周边'),
                          ('other', '其它'), ('mail_steamer', '邮轮'))
    #合同类别
    contractTypeItems = (('native','国内游'),('abroad','国外游'),('one_day','一日游'),('Taiwan','台湾游'))
    #扣点
    deduction_point_items = (('percent','百分比'),('price','人头数'))

    isLock = models.CharField(choices=isLockItems, default='active',max_length=20,verbose_name='状态')
    lineType = models.CharField(default='native',max_length=10, choices=lineTypeItems,verbose_name='产品类型')
    cnName = models.CharField(max_length=100,verbose_name='类别名称')
    code = models.CharField(max_length=200, verbose_name='英文名称')
    lineNum = models.IntegerField(default=0, verbose_name='线路数量')
    contract_type = models.CharField(default='native',max_length=10,choices=contractTypeItems,verbose_name='合同类型')
    point = models.CharField(default='0',max_length=100,verbose_name='扣点')
    bySort = models.IntegerField(default=0,verbose_name='权重')
    tags = models.CharField(null=True, blank=True,max_length=50,verbose_name='标签信息')
    detail = models.TextField(null=True,blank=True,verbose_name='内容')
    cpyLineNum = models.IntegerField(default=0,verbose_name='供应商数量')
    addTime = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    erpid = models.IntegerField(default=1,verbose_name='ERP_ID')
    img = models.CharField(default='这是img字段',max_length=200,verbose_name='img字段')
    admID = models.IntegerField(default=15447,verbose_name='admID字段')
#
#
# class BaseLineTravel(models.Model):
#     """行程模板"""
#     status_items = (('active', '启用'), ('forbidden', '禁用'))
#     share_status_items = (('active', '共享'), ('forbidden', '不共享'))
#
#     status = models.CharField(choices=status_items,verbose_name='状态')
#     track_summary = models.CharField(max_length=500,verbose_name='行程摘要')
#     dinner = models.CharField(max_length=500, verbose_name='用餐')
#     stay = models.CharField(max_length=500,verbose_name='住宿')
#     traffic = models.CharField(max_length=500,verbose_name='交通')
#     remarks = models.CharField(max_length=500,verbose_name='备注')
#     adder = models.ForeignKey(UserProfile,on_delete=None,verbose_name='添加人')
#     content = models.TextField(verbose_name='行程内容')


class BaseLine(models.Model):
    """线路"""
    status_items = (('active', '启用'), ('forbidden', '禁用'))

    status = models.CharField(default='active',choices=status_items, max_length=20)
    line_category = models.ForeignKey(LineCategory,on_delete=None)
    product_code = models.CharField(max_length=50,verbose_name='产品代码')
    name = models.CharField(max_length=100, verbose_name='产品名称')
    add_time = models.DateTimeField(default=datetime.now)