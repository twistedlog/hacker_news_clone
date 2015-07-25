from django.shortcuts import render
from django.views.generic import ListView
from .models import NewsItem
# Create your views here.

class NewsItemListView(ListView):
    template_name = "newsfeed/news_item_list.html"
    paginate_by = 20
    context_object_name = 'news_items'
    model = NewsItem

