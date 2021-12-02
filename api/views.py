from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Facebook
from .serializers import FacebookSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def facebook_api(request):
 if request.method == 'GET':
  id = request.data.get('id')
  if id is not None:
   fac = Facebook.objects.get(id=id)
   serializer = FacebookSerializer(fac)
   return Response(serializer.data)

  fac = Facebook.objects.all()
  serializer = FacebookSerializer(fac, many=True)
  return Response(serializer.data)

 if request.method == 'POST':
  serializer = FacebookSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Created'})
  return Response(serializer.errors)

 

 if request.method == 'PUT':
  id = request.data.get('id')
  fac = Facebook.objects.get(pk=id)
  serializer = FacebookSerializer(fac, data=request.data, partial=True)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Updated'})
  return Response(serializer.errors)

 if request.method == 'DELETE':
  id = request.data.get('id')
  fac = Facebook.objects.get(pk=id)
  fac.delete()
  return Response({'msg':'Data Deleted'})
 

 


 
