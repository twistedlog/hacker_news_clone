from datetime import datetime 

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class NewsItem(models.Model):
    url = models.URLField(unique=True)
    hn_url = models.URLField(null=True)
    posted_on = models.DateTimeField()
    upvotes = models.IntegerField()
    comments = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
         return "url: {0}, hn_url: {1}, upvotes: {2}, comments: {3}, posted_on: {4}".format(
             self.url, self.hn_url, self.upvotes, self.comments, self.posted_on)
      
    
    
class UserNewsItemTrack(models.Model):
    user = models.ForeignKey(User)
    news_item = models.ForeignKey(NewsItem)
    read = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ("user", "news_item")
  
    def save(self, *args, **kwargs):
        super(UserNewsItemTrack, self).save(*args, **kwargs)
  
