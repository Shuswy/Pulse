from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from monitor.models import TrackedTarget
from .filters import TargetFilter
from .serializers import TrackedTargetSerializer


class TrackedTargetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TrackedTarget.objects.all()
    serializer_class = TrackedTargetSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = TargetFilter
    search_fields = ['name', 'url']
    ordering_fields = ['last_scraped_at', 'name']
