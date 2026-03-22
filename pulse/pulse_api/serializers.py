from rest_framework import serializers
from monitor.models import TrackedTarget, PriceHistory


class PriceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceHistory
        fields = ['price', 'timestamp', 'raw_content_id']


class TrackedTargetSerializer(serializers.ModelSerializer):
    history = PriceHistorySerializer(many=True, read_only=True, source='pricehistory_set')

    class Meta:
        model = TrackedTarget
        fields = ['id', 'name', 'url', 'last_scraped_at', 'history']
