from django.db import models
from django.conf import settings

class Rating(models.Model):
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    score = models.PositiveSmallIntegerField()  # e.g. 1-5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service.name} - {self.score}"