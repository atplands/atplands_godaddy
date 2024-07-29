from django.db import models
from datetime import datetime
from embed_video.fields import EmbedVideoField
from realtors.models import Realtor

class Carausel(models.Model):
  image = models.ImageField(upload_to='pics/%y/%m/%d/')
  title = models.CharField(max_length=150)
  sub_title = models.CharField(max_length=100)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title

class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  mapframe=models.CharField(max_length=400, default= "MapFrame Tags" , blank=True , null=True)
  address = models.CharField(max_length=400)
  Longitude = models.DecimalField(max_digits=10, decimal_places=8 ,default=77.5980 , blank=True , null=True)
  Latitude = models.DecimalField(max_digits=10, decimal_places=8 ,default=14.8008 , blank=True , null=True)
  type = models.CharField(max_length=200 ,default= "AL" , blank=True , null=True)
  city = models.CharField(max_length=100)
  division = models.CharField(max_length=200 ,default= "ARM" , blank=True , null=True)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  bedrooms = models.DecimalField(max_digits=5, decimal_places=3 ,default=0.10, blank=True , null=True)
  bathrooms = models.IntegerField(default=1 , blank=True , null=True)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=3)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  video_url = EmbedVideoField(blank=True)
  def __str__(self):
    return self.title

# Model for Services
class Service(models.Model):
    service_name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True)
    photo_service = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    service_type = models.CharField(
        max_length=50,
        choices=[
            ('home_loan', 'Home Loan'),
            ('interior_design', 'Interior Design'),
            ('building_materials', 'Building Materials'),
	    ('personal_loan', 'Personal Loan'),
            ('house_design', 'House Design'),
            ('building_contractor', 'Building Contractor'),

            # Add more service types as needed
        ]
    )
    contact_email = models.EmailField(blank=True)
    contact_phone = models.IntegerField()
    
    def __str__(self):
        return self.service_name