"""erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url

from .views_test import TestView
from .views import TestView,LineCategoryView,APITestView,BaseLineView

urlpatterns = [
    url(r'^test$', LineCategoryView.as_view(), name='test'),
    url(r'^testview$', APITestView.as_view(), name='test_view'),
    url(r'^createbaseline$', BaseLineView.as_view(), name='base_line'),
]