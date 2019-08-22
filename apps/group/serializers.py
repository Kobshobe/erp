import os
import sys
pwd = os.path.dirname(os.path.realpath(__file__)) #获取当前目录
sys.path.append(pwd + "../../")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp.settings')

from rest_framework import serializers

from group.models import TestModel, LineCategory, BaseLine


# def creatLineCategory():
#     # for k,v in line_category:
#     l = TestModel.objects.create(name='Tom', age=23)


class LineCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LineCategory
        fields = '__all__'


class BaseLineSerializer(serializers.ModelSerializer):
    line_category = LineCategorySerializer()
    class Meta:
        model = BaseLine
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'