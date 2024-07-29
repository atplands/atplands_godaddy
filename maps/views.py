from django.shortcuts import render
#from django.shortcuts import get_object_or_404, render
#from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import folium

#from .models import Video
from listings.models import Listing
#from listings import views as views_map

# Create your views here.
def Map_index(request):
  
  al_listings = Listing.objects.order_by('-list_date').filter(is_published=True).filter(type__iexact="AL")
  vp_listings = Listing.objects.order_by('-list_date').filter(is_published=True).filter(type__iexact="VP")
  cl_listings = Listing.objects.order_by('-list_date').filter(is_published=True).filter(type__iexact="CL")
  hr_listings = Listing.objects.order_by('-list_date').filter(is_published=True).filter(type__iexact="HR")
  fh_listings = Listing.objects.order_by('-list_date').filter(is_published=True).filter(type__iexact="FH")

  map = folium.Figure( height=500)
  map1 = folium.Map(location=[14.681190,77.596700],zoom_start=9,width='100%', height='100%',control_scale=True,min_zoom = 2,).add_to(map)
  for i in al_listings:
    listing_id = str(i.id)
    lat  = str(i.Latitude)
    long = str(i.Longitude)
    title = str(i.title)
    price = str(i.price)
    photo_url = i.photo_main.url
    photo_1_url = "/media/" + str(i.photo_2) 
    photo_2_url = "/media/" + str(i.photo_3)
    photo_3_url = "/media/" + str(i.photo_4)


    popup_txt1 = f"""
          <div class="d-flex" style=" overflow: auto; height: auto;  width: 120px;display: flex;">
              <img src="{photo_url}" class="col" alt="Listing Photo" style="object-fit:cover; width: auto; height:88px;">
              <img src="{photo_1_url}" class="col" alt="Listing Photo1" style="object-fit:cover; width: auto; height:88px;">
              <img src="{photo_2_url}" class="col" alt="Listing Photo2" style="object-fit:cover; width: auto; height:88px;">
              <img src="{photo_3_url}" class="col" alt="Listing Photo3" style="object-fit:cover; width: auto; height:88px;">
          </div>
                """
        
    tooltip_txt = f'<p>AL: "{title}" <br> Price: "{price}"</p>'
    popup_txt = f'<img src="{photo_url}" width="auto" height="64"/>'
    url = f'http://atplands.com/listings/{listing_id}'
    popup_txt_link = popup_txt1 + f'<br> <a href="{url}"' + 'target="_blank">' + title + '</a>'
    marker = folium.Marker([lat,long], tooltip=tooltip_txt ,popup=popup_txt_link,
                         icon=folium.Icon(color='green',icon='ok-sign')).add_to(map1)
  for i in cl_listings:
    listing_id = str(i.id)
    lat  = str(i.Latitude)
    long = str(i.Longitude)
    title = str(i.title)
    price = str(i.price)
    photo_url = i.photo_main.url
    photo_1_url = "/media/" + str(i.photo_2) 
    photo_2_url = "/media/" + str(i.photo_3)
    photo_3_url = "/media/" + str(i.photo_4)
    #home = str(i.home_number)
    #loc_list.append(city +" "+  street +" "+ home)
    #img = i.header_img
    #img_list.append(img)
    popup_txt1 = f"""
          <div class="d-flex" style=" overflow: auto; height: auto;  width: 120px;display: flex;">
              <img src="{photo_url}" class="col" alt="Listing Photo" style="object-fit:cover; width: auto; height:88px;">
              <img src="{photo_1_url}" class="col" alt="Listing Photo1" style="object-fit:cover; width: auto; height:88px;">
              <img src="{photo_2_url}" class="col" alt="Listing Photo2" style="object-fit:cover; width: auto; height:88px;">
              <img src="{photo_3_url}" class="col" alt="Listing Photo3" style="object-fit:cover; width: auto; height:88px;">
          </div>
                """
        
    tooltip_txt = f'<p>CL: "{title}" <br> Price: "{price}"</p>'
    popup_txt = f'<img src="{photo_url}" width="auto" height="64"/>'
    url = f'http://atplands.com/listings/{listing_id}'
    popup_txt_link = popup_txt1 + f'<br> <a href="{url}"' + 'target="_blank">' + title + '</a>'
    marker = folium.Marker([lat,long], tooltip=tooltip_txt ,popup=popup_txt_link,
                         icon=folium.Icon(color='darkgreen',icon='ok-sign')).add_to(map1)
  for i in vp_listings:
    listing_id = str(i.id)
    lat  = str(i.Latitude)
    long = str(i.Longitude)
    title = str(i.title)
    price = str(i.price)
    photo_url = i.photo_main.url
    photo_1_url = "/media/" + str(i.photo_2) 
    photo_2_url = "/media/" + str(i.photo_3)
    photo_3_url = "/media/" + str(i.photo_4)
    #home = str(i.home_number)
    #loc_list.append(city +" "+  street +" "+ home)
    #img = i.header_img
    #img_list.append(img)
    popup_txt1 = f"""
          <div class="d-flex" style=" overflow: auto; height: auto;  width: 120px;display: flex;">
              <img src="{photo_url}" class="col" alt="Listing Photo" style="object-fit:cover; width: auto; height:88px;">
              <img src="{photo_1_url}" class="col" alt="Listing Photo1" style="object-fit:cover; width: auto; height:88px;">
              <img src="{photo_2_url}" class="col" alt="Listing Photo2" style="object-fit:cover; width: auto; height:88px;">
              <img src="{photo_3_url}" class="col" alt="Listing Photo3" style="object-fit:cover; width: auto; height:88px;">
          </div>
                """
        
    tooltip_txt = f'<p>VP: "{title}" <br> Price: "{price}"</p>'
    popup_txt = f'<img src="{photo_url}" width="auto" height="64"/>'
    url = f'http://atplands.com/listings/{listing_id}'
    popup_txt_link = popup_txt1 + f'<br> <a href="{url}"' + 'target="_blank">' + title + '</a>'
    marker = folium.Marker([lat,long], tooltip=tooltip_txt ,popup=popup_txt_link,
                         icon=folium.Icon(color='pink',icon='ok-sign')).add_to(map1)
  for i in fh_listings:
    listing_id = str(i.id)
    lat  = str(i.Latitude)
    long = str(i.Longitude)
    title = str(i.title)
    price = str(i.price)
    photo_url = i.photo_main.url
    photo_1_url = "/media/" + str(i.photo_2) 
    photo_2_url = "/media/" + str(i.photo_3)
    photo_3_url = "/media/" + str(i.photo_4)
    #home = str(i.home_number)
    #loc_list.append(city +" "+  street +" "+ home)
    #img = i.header_img
    #img_list.append(img)
    popup_txt1 = f"""
          <div class="d-flex" style=" overflow: auto; height: auto;  width: 120px;display: flex;">
              <img src="{photo_url}" class="col" alt="Listing Photo" style="object-fit:cover; width: auto; height:88px;">
              <img src="{photo_1_url}" class="col" alt="Listing Photo1" style="object-fit:cover; width: auto; height:88px;">
              <img src="{photo_2_url}" class="col" alt="Listing Photo2" style="object-fit:cover; width: auto; height:88px;">
              <img src="{photo_3_url}" class="col" alt="Listing Photo3" style="object-fit:cover; width: auto; height:88px;">
          </div>
                """
    tooltip_txt = f'<p>FH: "{title}" <br> Price: "{price}"</p>'
    popup_txt = f'<img src="{photo_url}" width="auto" height="64"/>'
    url = f'http://atplands.com/listings/{listing_id}'
    popup_txt_link = popup_txt1 + f'<br> <a href="{url}"' + 'target="_blank">' + title + '</a>'
    marker = folium.Marker([lat,long], tooltip=tooltip_txt ,popup=popup_txt_link,
                         icon=folium.Icon(color='blue',icon='ok-sign')).add_to(map1)
  for i in hr_listings:
    listing_id = str(i.id)
    lat  = str(i.Latitude)
    long = str(i.Longitude)
    title = str(i.title)
    price = str(i.price)
    photo_url = i.photo_main.url
    photo_1_url = "/media/" + str(i.photo_2) 
    photo_2_url = "/media/" + str(i.photo_3)
    photo_3_url = "/media/" + str(i.photo_4)
    #home = str(i.home_number)
    #loc_list.append(city +" "+  street +" "+ home)
    #img = i.header_img
    #img_list.append(img)
    popup_txt1 = f"""
          <div class="d-flex" style=" overflow: auto; height: auto;  width: 120px;display: flex;">
              <img src="{photo_url}" class="col" alt="Listing Photo" style="object-fit:cover; width: auto; height:88px;">
              <img src="{photo_1_url}" class="col" alt="Listing Photo1" style="object-fit:cover; width: auto; height:88px;">
              <img src="{photo_2_url}" class="col" alt="Listing Photo2" style="object-fit:cover; width: auto; height:88px;">
              <img src="{photo_3_url}" class="col" alt="Listing Photo3" style="object-fit:cover; width: auto; height:88px;">
          </div>
                """
        
    tooltip_txt = f'<p>HR: "{title}" <br> Price: "{price}"</p>'
    popup_txt = f'<img src="{photo_url}" width="auto" height="64"/>'
    url = f'http://atplands.com/listings/{listing_id}'
    popup_txt_link = popup_txt1 + f'<br> <a href="{url}"' + 'target="_blank">' + title + '</a>'
    marker = folium.Marker([lat,long], tooltip=tooltip_txt ,popup=popup_txt_link,
                         icon=folium.Icon(color='orange',icon='ok-sign')).add_to(map1)


  #map1 = folium.Map(location=[14.681190,77.596700],zoom_start=9,)
  #popup1 = "<a href="+ "" +">Palm Country Venture" +"</a>"

  #marker = folium.Marker(data_list,popup=popup1,tooltip="Palm Country venture 5.8L")
  marker.add_to(map1)
  map1 = map1._repr_html_()
  #map_listings = Listing.objects.order_by('-added')
  #paginator = Paginator(map_listings, 6)
  #page = request.GET.get('page')
  #video_paged_listings = paginator.get_page(page)

  context = {
    #'video_listings': video_paged_listings,
    'map1':map1
  }

  return render(request, 'maps/maps.html', context)
