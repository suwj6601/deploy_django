# vercel_app/urls.py
from django.urls import path, include

urlpatterns = [
    path('', include('example.urls')),
]