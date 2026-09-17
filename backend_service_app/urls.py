
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/accounts/',include('accounts.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/services/', include('services.urls')),
    path('api/ratings/', include('ratings.urls')),
]
