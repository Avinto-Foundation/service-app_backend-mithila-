import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_service_app.settings')
django.setup()

from services.models import Service

image_updates = {
    "Sarah's Plumbing Co.": "https://loremflickr.com/400/300/plumber?lock=1",
    "QuickFix Plumbers": "https://loremflickr.com/400/300/plumber?lock=2",
    "AquaFlow Plumbing": "https://loremflickr.com/400/300/plumber?lock=3",
    "Bright Spark Electric": "https://loremflickr.com/400/300/electrician?lock=4",
    "PowerPro Electrical": "https://loremflickr.com/400/300/electrician?lock=5",
    "Sparkle Home Cleaning": "https://loremflickr.com/400/300/cleaning?lock=6",
    "Deep Clean Squad": "https://loremflickr.com/400/300/cleaning?lock=7",
    "GreenScape Landscaping": "https://loremflickr.com/400/300/landscaping?lock=8",
    "Fresh Coat Painters": "https://loremflickr.com/400/300/painter?lock=9",
    "ColorWorks Painting Co.": "https://loremflickr.com/400/300/painter?lock=10",
    "MoveIt Haulers": "https://loremflickr.com/400/300/movers?lock=11",
    "Reliable Movers": "https://loremflickr.com/400/300/movers?lock=12",
}

updated = 0
for name, url in image_updates.items():
    updated += Service.objects.filter(name=name).update(image_url=url)

print(f"Updated {updated} service image URLs.")