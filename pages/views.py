from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import devision_choices, price_choices, type_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:10]
    al_listings = Listing.objects.order_by('-list_date').filter(is_published=True).filter(type__iexact="AL")
    vp_listings = Listing.objects.order_by('-list_date').filter(is_published=True).filter(type__iexact="VP")
    cl_listings = Listing.objects.order_by('-list_date').filter(is_published=True).filter(type__iexact="CL")
    hr_listings = Listing.objects.order_by('-list_date').filter(is_published=True).filter(type__iexact="HR")
    fh_listings = Listing.objects.order_by('-list_date').filter(is_published=True).filter(type__iexact="FH")


    context = {
        'listings': listings,
        'al_listings': al_listings,
        'vp_listings': vp_listings,
        'cl_listings': cl_listings,
        'hr_listings': hr_listings,
        'fh_listings': fh_listings,
        'devision_choices':devision_choices,
        'state_choices': state_choices,
        'type_choices': type_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)