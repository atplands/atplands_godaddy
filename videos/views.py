from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Video

# Create your views here.
def Video_index(request):
  video_listings = Video.objects.order_by('-added')
  paginator = Paginator(video_listings, 6)
  page = request.GET.get('page')
  video_paged_listings = paginator.get_page(page)

  context = {
    'video_listings': video_paged_listings
  }

  return render(request, 'videos/videos.html', context)
