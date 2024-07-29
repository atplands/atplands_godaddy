from django.db import models

# Create your models here.
from embed_video.fields import EmbedVideoField
from listings.models import Listing

class Video(models.Model):

    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    #listing = models.CharField(max_length=500, default='Sai Ventures')
    title =models.CharField(max_length=500)
    added = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=100000 , blank=True, null=True)
    bedrooms = models.IntegerField(default=1 ,blank=True, null=True)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1 ,default=1 ,blank=True, null=True)
    garage = models.IntegerField(default=1 ,blank=True, null=True)
    city = models.CharField(max_length=100 , default="Anantapur" ,blank=True, null=True)
    state = models.CharField(max_length=100 , default="Anantapur" ,blank=True, null=True)
    zipcode = models.CharField(max_length=20 ,default=515001 ,blank=True, null=True)
    url = EmbedVideoField()  # same like models.URLField()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-added']
