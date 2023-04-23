from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .faker_to_add_data import start
from .models import TbPatientInfo

from rest_framework import serializers

class UserVerifyOtpSerializer(serializers.ModelSerializer):

    class Meta:
      model = TbPatientInfo
      fields = '__all__'


# Create your views here.
class TestApiView(APIView):
    serializer_class = UserVerifyOtpSerializer
    def post(self, request, format=None):
        serializer = UserVerifyOtpSerializer(data = request.data )
        serializer.is_valid(raise_exception=True)
        item = serializer.save()
        
        data = serializer.data
        return Response({'msg': 'Post Data', 'data': data}, status=status.HTTP_200_OK)

    def get(self, request, format=None):
        #start()
        return Response({'msg': 'message', 'is_email': 'is_email'}, status=status.HTTP_200_OK)