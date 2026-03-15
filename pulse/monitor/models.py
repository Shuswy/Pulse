from django.db import models


class Website(models.Model):
    """Parent entity"""
    name = models.CharField(max_length=100)
    base_url = models.URLField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TrackedTarget(models.Model):
    """Specific item being tracked"""
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='targets')
    name = models.CharField(max_length=255)
    url = models.URLField()
    css_selector = models.CharField(max_length=500)
    interval = models.PositiveIntegerField(default=60) # In minutes
    last_scraped_at = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} on {self.website.name}"


class PriceHistory(models.Model):
    """Record of findings"""
    target = models.ForeignKey(TrackedTarget, on_delete=models.CASCADE, related_name='history')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    # Link raw HTML to price
    raw_content_id = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
