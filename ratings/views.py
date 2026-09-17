from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Rating
from .serializers import RatingSerializer

@api_view(['GET'])
def rating_list(request):
    ratings = Rating.objects.select_related('service', 'service__category', 'user').all()
    serializer = RatingSerializer(ratings, many=True)
    return Response({"data": serializer.data}, status=status.HTTP_200_OK)