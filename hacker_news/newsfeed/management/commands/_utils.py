from django.conf import settings

def format_item_url(item):
    return settings.HN_ITEM_URL.format(item_id=item)