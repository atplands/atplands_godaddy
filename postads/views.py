from django.shortcuts import redirect,render
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import Postad

# Create your views here.

def index(request):
    if request.method == 'POST':
        owner_type = request.POST['owner_type']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        title = request.POST['title']
        address = request.POST['address']
        message = request.POST['message']
        user_id = request.POST['user_id']
        if len(request.FILES) != 0:
            uploaded_file = request.FILES['photo_main']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)

        #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_postad = Postad.objects.all().filter(title=title, user_id=user_id)
            if has_postad:
                messages.error(request, 'You have already Post Ad for this listing')
                return redirect('dashboard')

        postad = Postad(owner_type=owner_type, name=name, email=email, phone=phone, title=title ,address=address ,message=message, photo_main=uploaded_file ,user_id=user_id )

        postad.save()

    # Send email
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   'iprabhatdev@gmail.com',
    #   [realtor_email, 'random@gmail.com'],
    #   fail_silently=False
    # )

        messages.success(request, 'Your Property has been submitted, Property will be published in 12 Hrs in Home page.')
        return redirect('dashboard')
    return redirect('index')
