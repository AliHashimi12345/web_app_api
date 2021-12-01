from django.shortcuts import render
from .models import Facebook
from .serializers import FacebookSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.
def facebook_detail(request,pk):
    fac = Facebook.objects.get(id = pk)
    #print(fac)
    serializer = FacebookSerializer(fac)
    #print(serializer)
    #print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data, content_type='application/json')

# Query Set - All  Data
def facebook_list(request):
    fac = Facebook.objects.all()
    serializer = FacebookSerializer(fac, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


 
