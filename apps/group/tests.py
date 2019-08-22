from datetime import datetime
from django.test import TestCase
import json
from django.http import HttpRequest
from django.urls import resolve
from django.template.loader import render_to_string
from rest_framework.test import APITestCase

from .models import TestModel, LineCategory, BaseLine


class GroupTest(APITestCase):
    """"""
    def setUp(self):
        print('--------------begin-----------------')

    def tearDown(self):
        print('--------------finish----------------')

    # def test_view(self):
    #     TestModel.objects.create(name='Jonnay', age=23)
    #     found = self.client.get('/groups/testview')
    #     self.assertEqual(found.status_code, 200)
    #     print(type(found))
    #     print(found.data)

    def test_create_line_category(self):
        '''新建线路'''

        # ------------------OP陈思杰创建新线路：DRF泰国跟团游
        print('##-- 新建线路类别：“DRF泰国跟团游” --##')
        found = self.client.post('/groups/test',{'type_name':'DRF泰国跟团游', 'type_en_name':'DRF Thailang Trip',
                                                 'tag_info':'DRF泰国,DRF跟团境外'})

        self.assertEqual(found.status_code, 201)
        new_line_category = LineCategory.objects.get(type_name='DRF泰国跟团游')
        print(new_line_category)
        self.assertEqual(new_line_category.type_name, 'DRF泰国跟团游', msg='线路类别名称测试')
        self.assertEqual(new_line_category.type_en_name, 'DRF Thailang Trip')
        self.assertEqual(new_line_category.tag_info, 'DRF泰国,DRF跟团境外')
        self.assertEqual(new_line_category.status, 'active')
        self.assertEqual(new_line_category.product_type, 'native')
        self.assertEqual(new_line_category.type_account, 0)
        self.assertEqual(new_line_category.contract_type, 'native')
        self.assertEqual(new_line_category.deduction_point, '0')
        self.assertEqual(new_line_category.weight, 0)
        self.assertEqual(new_line_category.content, None)
        self.assertEqual(new_line_category.supplier_amount, 0)
        self.assertAlmostEquals((datetime.now() - new_line_category.add_time).seconds, 0.5, delta=1)
        print('##-- 新建线路类别成功 --##')

        # ------------------OP陈思杰创建新线路产品：DRF泰国3天2晚跟团游
        # status = models.CharField(default='active', choices=status_items, max_length=20)
        # line_category = models.ForeignKey(LineCategory, on_delete=None)
        # product_code = models.CharField(max_length=50, verbose_name='产品代码')
        # name = models.CharField(max_length=100, verbose_name='产品名称')
        # add_time = models.DateTimeField(default=datetime.now)

        print('##-- 新建线路产品：“DRF泰国3天2晚跟团游” --##')
        line_category = LineCategory.objects.get(type_name='DRF泰国跟团游')
        new_line_product = BaseLine.objects.create(line_category=line_category,product_code='DRF_TG_4D3N',
                                                   name='DRF泰国3天2晚跟团游',)

        found = self.client.get('/groups/createbaseline')
        self.assertEqual(found.status_code, 200)

        self.assertEqual(new_line_product.name, 'DRF泰国3天2晚跟团游')
        print('##-- 新建线路产品成功 --##')