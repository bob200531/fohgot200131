from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

# def UsersManualList(request):
#     manul_users = User.objects.all()
#     serializers = UsersManualSerializers(manul_users,many=True)
#     return Response(serializers.data)

@api_view(['GET'])
def UsersManualList(request):
    manual_users = User.objects.all()
    serializer = UsersManualSerializers(manual_users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def UsersManyalDetail(request,pk):
    manyal_detail = User.objects.get(pk=pk)
    serializer = UsersManualSerializers(manyal_detail)
    return Response(serializer.data)