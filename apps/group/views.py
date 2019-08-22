from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic.base import View
from django.http import HttpResponse,JsonResponse

from .models import LineCategory,TestModel,BaseLine
from .serializers import LineCategorySerializer,TestSerializer,BaseLineSerializer


class LineCategoryView(APIView):
    """
    List all LineCategory
    """
    def get(self, request, format=None):
        lind_category = LineCategory.objects.all()[:10]
        lind_category_serializer = LineCategorySerializer(lind_category, many=True)
        return Response(lind_category_serializer.data)

    def post(self, request, format=None):
        serializer = LineCategorySerializer(data=request.data)
        # print(request.data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer.create(request.data))
            data = LineCategory.objects.filter(type_name=serializer.data['type_name'])
            data_serializer = LineCategorySerializer(data, many=True)
            print(data_serializer.data)
            return Response(data_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BaseLineView(APIView):
    def get(self, request, format=None,):
        base_line = BaseLine.objects.all()[:10]
        base_line_serializer = BaseLineSerializer(base_line, many=True)
        return Response(base_line_serializer.data)

    def post(self,request):
        return HttpResponse('11111111111')


class TestView(View):
    def get(self,request):
        return JsonResponse({'name':'Jonnay','age':23},)


class APITestView(APIView):
    def get(self,request, format=None):
        # TestModel.objects.create(name='Jonnay', age=23)
        test = TestModel.objects.all()[:10]
        test_serializer = TestSerializer(test, many=True)
        # print(type(test_serializer.data))
        return Response(test_serializer.data)