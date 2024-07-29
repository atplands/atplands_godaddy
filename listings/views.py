from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, devision_choices, state_choices ,type_choices
from .mapbox import mapbox_tokenkey

from .models import Listing

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)
  AL_listings = Listing.objects.order_by('-list_date').filter(is_published=True)
  LL_listings = Listing.objects.order_by('-list_date').filter(is_published=True)
  LP_listings = Listing.objects.order_by('-list_date').filter(is_published=True)
  HR_listings = listings.filter(type__iexact=type)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  paginator = Paginator(AL_listings, 6)
  page = request.GET.get('page')
  paged_al_listings = paginator.get_page(page)

  paginator = Paginator(LL_listings, 6)
  page = request.GET.get('page')
  paged_ll_listings = paginator.get_page(page)

  paginator = Paginator(LP_listings, 6)
  page = request.GET.get('page')
  paged_lp_listings = paginator.get_page(page)

  paginator = Paginator(HR_listings, 6)
  page = request.GET.get('page')
  paged_hr_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings,
    'al_listings': paged_al_listings,
    'll_listings': paged_ll_listings,
    'lp_listings': paged_lp_listings,
    'hr_listings': paged_hr_listings,
  }

  return render(request, 'listings/listings.html', context)

def videos_index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/videos.html', context)


def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
    'listing': listing,
    'mapbox_tokenkey':mapbox_tokenkey,
  }

  return render(request, 'listings/listing.html', context)

def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(division__iexact=state)

  # Type
  if 'type' in request.GET:
    type = request.GET['type']
    if type:
      queryset_list = queryset_list.filter(type__iexact=type)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'state_choices': state_choices,
    'type_choices': type_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)

def landtype(request, type):
  queryset_list = Listing.objects.order_by('-list_date')
  queryset_list = queryset_list.filter(type__iexact=type)

  context = {
    'state_choices': state_choices,
    'type_choices': type_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
  }

  return render(request, 'listings/search.html', context)

def landdivision(request, division):
  queryset_list = Listing.objects.order_by('-list_date')
  queryset_list = queryset_list.filter(division__iexact=state)

  context = {
    'state_choices': state_choices,
    'type_choices': type_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
  }

  return render(request, 'listings/search.html', context)