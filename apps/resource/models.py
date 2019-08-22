# from django.db import models
#
# # Create your models here.
#
#
# class CommonInfo(models.Model):
#     """常用信息"""
#     items = (
#         ('begin_and_end_city','起止城市'),('market_area','市场划分'),('order_type'),
#         ('common_items','常用文字'),('visa_consulate','签证领馆'),('company_title','公司抬头')
#     )
#
#     name = models.CharField(choices=items,verbose_name='常用信息名称')
#
#     class Meta:
#         verbose_name = '常用信息'
#         verbose_name_plural = verbose_name
#
#
# class BeginAndEndCity(models.Model):
#     status_items = (('active', '正常'), ('forbidden', '锁定'))
#
#     items_type = models.ForeignKey(CommonInfo,on_delete=None)
#     name = models.CharField(max_length=50,verbose_name='起止城市')
#     city_code = models.CharField(max_length=50,verbose_name='城市代码')
#     is_hot_city = models.BooleanField(verbose_name='是否热门')
#     status = models.CharField(choices=status_items,max_length=10)
#     level = models.IntegerField(max_length=9)
#     departure_city = models.CharField(max_length=20)
#
