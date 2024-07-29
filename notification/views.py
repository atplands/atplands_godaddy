import imp
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from notification.models import Notification

@login_required
def ShowNotification(request):
    user = request.user
    all_users = User.objects.all()
    notifications = Notification.objects.filter(user=user).order_by('-date')

    context = {
        'notifications': notifications,
        'all_users':all_users,

    }
    return render(request, 'landbook/notifications/notification.html', context)
    
@login_required
def DeleteNotification(request, noti_id):
    user = request.user    
    Notification.objects.filter(id=noti_id, user=user).delete()
    return redirect('show-notification')
