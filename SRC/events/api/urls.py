from rest_framework import routers
from django.urls import path, include
from .views import EventViewSet


router = routers.DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
