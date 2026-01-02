from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# 1. Create a router and register our ViewSet
router = DefaultRouter()
router.register(r'', TaskViewSet, basename='task')

# 2. The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]