from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from authy.views import UserProfile, follow

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('contacts/', include('contacts.urls')),
    path('videos/', include('videos.urls')),
    path('maps/', include('maps.urls')),
    path('users/', include('authy.urls')),
    path('post/', include('post.urls')),
    path('postads/', include('postads.urls')),
    path('message/', include('directs.urls')),
    path('notifications/', include('notification.urls')),

    # profile
    path('profile/<username>/', UserProfile, name='profile'),
    path('profile/<username>/saved/', UserProfile, name='profilefavourite'),
    path('profile/<username>/follow/<option>/', follow, name='follow'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)