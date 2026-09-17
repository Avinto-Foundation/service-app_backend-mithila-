from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name', read_only=True)
    category_label = serializers.CharField(source='service.category.label', read_only=True)
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Rating
        fields = [
            'id', 'service', 'service_name', 'category_label',
            'user', 'score', 'comment', 'created_at'
        ]