from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg, Count
from .models import Rating

def update_service_stats(service):
    agg = service.ratings.aggregate(avg=Avg('score'), count=Count('id'))
    service.rating = agg['avg'] or 0
    service.review_count = agg['count'] or 0
    service.save(update_fields=['rating', 'review_count'])

@receiver(post_save, sender=Rating)
def on_rating_save(sender, instance, **kwargs):
    update_service_stats(instance.service)

@receiver(post_delete, sender=Rating)
def on_rating_delete(sender, instance, **kwargs):
    update_service_stats(instance.service)