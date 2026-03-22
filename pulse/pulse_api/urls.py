from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TrackedTargetViewSet

router = DefaultRouter()
router.register(r'targets', TrackedTargetViewSet, basename='target')

urlpatterns = [
    path('', include(router.urls))
]