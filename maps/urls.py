from django.urls import path

from . import views

urlpatterns = [
    path('', views.Map_index, name='maps'),
    #path('<int:listing_id>', views.listing, name='listing'),
    #path('search', views.search, name='search'),
]