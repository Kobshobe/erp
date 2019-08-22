import datetime
import json


from django.views.generic.base import View
from django.http import HttpResponse,JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers

from .models import LineCategory

class TestView(View):

    def get(self, request):
        group_info = LineCategory.objects.all()
        # group_info.add_time = datetime.datetime.now()
        # group_info.save()
        #方式1：普通
        # group = {}
        # group['name'] = group_info.product_type
        # group['status'] = group_info.status


        #方式2：model_to_dict
        # group = model_to_dict(group_info)
        # return HttpResponse(json.dumps(group), content_type='application/json')

        #方式3：serializers
        group = serializers.serialize('json', group_info)
        return HttpResponse(group, content_type='application/json')
        # group = json.loads(group)
        # return JsonResponse(group,safe=False)