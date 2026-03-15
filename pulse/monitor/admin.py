from django.contrib import admin

from .models import Website, TrackedTarget, PriceHistory


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_url', 'is_active')
    search_fields = ('name',)


@admin.register(TrackedTarget)
class TrackedTargetAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'interval', 'last_scraped_at', 'active')
    list_filter = ('website', 'active')
    search_fields = ('name', 'url')
    list_editable = ('active', 'interval')


@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ('target', 'price', 'timestamp')
    readonly_fields = ('timestamp',)
