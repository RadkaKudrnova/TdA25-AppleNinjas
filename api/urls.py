from django.urls import path
from .views import organization_api

urlpatterns = [
    path('api/', organization_api, name='organization_api'),
]