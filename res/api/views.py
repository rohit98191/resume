from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from .models import Required


# Create your views here.
class RequiredList(APIView):



    def get(self,request,format=None):
        off =Required.objects.all()
        serializer =RequiredSerializer(off,many=True)
        response=serializer.data
        return Response(response)

    def post(self, request, format=None):
        serializer = RequiredSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class RequiredDells(APIView):
    def get_object(self, pk):
        try:
            return Required.objects.get(pk=pk)
        except Required.DoesNotExist:
            return ("NO DATA")


    def get(self,request,pk,format=None):
        getter =self.get_object(pk)
        serializer =RequiredSerializer(getter)
        return Response(serializer.data)


