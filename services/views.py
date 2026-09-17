from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Service
from .serializers import ServiceSerializer

@api_view(['GET'])
def service_list(request):
    services = Service.objects.select_related('category').all()
    serializer = ServiceSerializer(services, many=True)
    return Response({"data": serializer.data}, status=status.HTTP_200_OK)