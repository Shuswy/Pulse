from celery import shared_task
from .models import TrackedTarget, PriceHistory
from .services import ScraperService
from django.utils import timezone
from .db_utils import MongoStorage

@shared_task(name="tasks.trigger_all_scrapes")
def trigger_all_scrapes():
    active_targets = TrackedTarget.objects.filter(active=True)

    for target in active_targets:
        scrape_product_task.delay(target.id)
    return f"Triggered {active_targets.count()} scrapes."

@shared_task(bind=True, name="tasks.scrape_product")
def scrape_product_task(self, target_id):
    try:
        target = TrackedTarget.objects.get(id=target_id)

        result = ScraperService.scrape_target(target)

        if result:
            mongo_store = MongoStorage()
            mongo_id = mongo_store.save_html(target.id, result['raw_html'])

            PriceHistory.objects.create(
                target=target,
                price=result['price'],
                raw_content_id=mongo_id
            )

            target.last_scraped_at = timezone.now()
            target.save()

            return f"Success: {target.name} is now {result['price']}"
        return f"Failed: No result for {target.name}"
    except TrackedTarget.DoesNotExist:
        return f"Error: Target {target_id} not found"