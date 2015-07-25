from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from .models import (NewsItem, UserNewsItemTrack)
# Create your views here.

class NewsItemListView(ListView):
    template_name = "newsfeed/news_item_list.html"
    paginate_by = 20
    context_object_name = 'news_items'
    model = NewsItem
    
    def get_queryset(self):
        qs = super(NewsItemListView, self).get_queryset()
        # get a list of items that have been marked deleted
        deleted_items = UserNewsItemTrack.objects.filter(
          user=self.request.user, deleted= True).values_list('news_item__id', flat=True)
      
        qs = qs.exclude(id__in=deleted_items)
      
        #TODO optimize this
        for row in qs:
            try:
                UserNewsItemTrack.objects.get(
                  news_item=row,
                  user=self.request.user, 
                  read=True)
            except ObjectDoesNotExist as e:
                row.read = False
            else:
                row.read = True
        return qs

    
class NewsItemReadView(View):
    http_method_names = ["post"]
    
    def post(self, request, *args, **kwargs):
        id = request.POST.get('item-id')
        news_item = NewsItem.objects.get(id=id)
        obj, created = UserNewsItemTrack.objects.get_or_create(
             user=request.user, news_item=news_item, read=True)
        return HttpResponse('ok')


class NewsItemDeleteView(View):
    http_method_names = ["post"]
    
    def post(self, request, *args, **kwargs):
        id = request.POST.get('item-id')
        news_item = NewsItem.objects.get(id=id)
        obj, created = UserNewsItemTrack.objects.get_or_create(
             user=request.user, news_item=news_item)
        if not obj.deleted:
            obj.deleted = True
            obj.save()
        return HttpResponse('ok')
