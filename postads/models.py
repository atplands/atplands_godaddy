from django.db import models
from datetime import datetime
from embed_video.fields import EmbedVideoField

class Postad(models.Model): 
  owner_type = models.CharField(max_length=200)
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=14)  
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=600)
  message = models.TextField(blank=True , null=True)  
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')  
  is_published = models.BooleanField(default=True)
  user_id = models.IntegerField(blank=True,null=True)
  video_url = EmbedVideoField(blank=True,null=True,default="https://www.youtube.com/watch?v=DL77F7AWIl8")  
  ad_date = models.DateTimeField(default=datetime.now)
  def __str__(self):
    return self.title
  
