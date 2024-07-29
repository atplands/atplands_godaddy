from django.contrib import admin
from .models import Postad

# Register your models here.


class PostadAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'title', 'email', 'ad_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'title')
  list_per_page = 25

admin.site.register(Postad, PostadAdmin)