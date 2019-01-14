from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('shoppinglist.urls')),
    path('', include('usermanagement.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
]
