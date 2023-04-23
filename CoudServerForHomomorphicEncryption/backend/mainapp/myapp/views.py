from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Max
from mainapp import settings
import pickle

class TLC(APIView):
    def post(self,request):
        if "params" in request.data:
            params=request.data["params"]
            if "x" in params and "y" in params:
                x=pickle.loads(bytes.fromhex(params["x"]))
                y=pickle.loads(bytes.fromhex(params["y"]))
                sum=x+y
                sum=pickle.dumps(sum).hex()
                return Response(data={"ans":sum})
        return Response(status=status.HTTP_400_BAD_REQUEST)  
class MHR(APIView):
    def post(self,request):
        if "params" in request.data:
            params=request.data["params"]
            if "x" in params and "y" in params:
                x=pickle.loads(bytes.fromhex(params["x"]))
                y=pickle.loads(bytes.fromhex(params["y"]))
                sum=x-y
                sum=pickle.dumps(sum).hex()
                return Response(data={"ans":sum})
            return Response(status=status.HTTP_400_BAD_REQUEST)  