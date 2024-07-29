from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('<str:type>', views.landtype, name='landtype'),
    path('<str:division>', views.landdivision, name='landdivision'),
    path('videos', views.videos_index, name='videos_listings'),
]