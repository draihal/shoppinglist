from django.urls import path, include
from . import views

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),

    path('settings/', views.settings, name='settings'),
    path('settings_github/', views.github_password,
         name='settings_github'),
    path('signup/', views.signup, name='signup'),
]
