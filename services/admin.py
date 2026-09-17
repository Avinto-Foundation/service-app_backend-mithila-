from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'rating', 'review_count', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'address')