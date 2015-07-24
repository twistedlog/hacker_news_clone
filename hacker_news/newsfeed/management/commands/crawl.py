import requests
import arrow

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import transaction, IntegrityError

from newsfeed.models import NewsItem
from _utils import format_item_url


class Command(BaseCommand):
    help = 'Crawls HN to get the latest {update_no} updates'.format(update_no=settings.UPDATE_NO)
    
    def handle(self, *args, **options):
        self._crawl()
    
    def _crawl(self):
        try:
            top_items = requests.get(settings.HN_TOP_ITEMS_URL)
        except Exception as e:
            pass
        # trucate the result to get top 90 enteries only
        top_items = top_items.json()[:settings.UPDATE_NO]
        print top_items
        self.fetch(top_items)
      
    def fetch(self, items):
        data = []
        for item in items:
             url = format_item_url(item)
             try:
                 item = requests.get(url)
             except Exception as e:
                 raise e
             else:
                 data.append({
                    "url": url, 
                    "data": item.json()
                 })
        data = self.clean(data)
        self.insert_or_update_data(data)
             
      
    def insert_or_update_data(self, data):
        try:
            with transaction.atomic():
                 for entry in data:    
                     obj, created = NewsItem.objects.update_or_create(
                         url=entry.pop("url"), defaults=entry)
        except IntegrityError as e:
            raise e
        else:
            pass
          
    def clean(self, data):
        result = []
        import pprint
        pprint.pprint(data)
        for row in data:
            _data = row.get("data")
            result.append({
                "url": row.get("url"),
                "hn_url": _data.get("url", None),
                "posted_on": arrow.get(_data.get("time")).datetime,
                "comments": len(_data.get("kids", [])),
                "upvotes": _data.get("score", 0)
            })
        return result