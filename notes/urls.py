from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, NoteViewSet, token_view

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', token_view, name='api_token_auth'),
]
