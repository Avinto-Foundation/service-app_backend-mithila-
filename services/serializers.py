from rest_framework import serializers
from .models import Service
from categories.serializers import CategorySerializer

class ServiceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'category', 'rating', 'review_count',
            'address', 'phone', 'image_url', 'price',
            'distance_miles', 'tags'
        ]