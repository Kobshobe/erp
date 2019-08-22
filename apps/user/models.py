# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
#
# # Create your models here.
# #
# # class UserAccount(models.Model):
# #
#
# class UserProfile(AbstractBaseUser):
#     """注册用户"""
#     jobs_items = (('finance','财务'),('seller','销售'),('assistant','助理'),
#                   ('line_operator','线路OP'),('ticket_operator','机票OP'),
#                   ('visa_operator','签证OP'),('hotel_operator','酒店OP'),
#                   ('local_operator','地接OP'))
#
#     name = models.CharField(max_length=50,verbose_name='登录账号')
#     real_name = models.CharField(max_length=50,verbose_name='真实姓名')
#     credit = models.IntegerField(max_length=9,verbose_name='授信额度')
#     # organization = models.CharField(max_length=50,verbose_name='所属组织')
#     # organization_operated = models.CharField(max_length=50,verbose_name='管理组织')
#     # staff_operaed = models.CharField(max_length=50)
#     # sell_range = models.CharField(max_length=50)
#     # check_level = models.CharField()
#     position = models.CharField(choices=jobs_items,verbose_name='所在岗位')
