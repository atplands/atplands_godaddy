from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from authy.views import UserProfile, EditProfile

urlpatterns = [
    # Profile Section
    path('profile/edit', EditProfile, name="editprofile"),

    # User Authentication
    path('sign-up/', views.register, name="sign-up"),
    path('sign-in/', auth_views.LoginView.as_view(template_name="landbook/sign-in.html", redirect_authenticated_user=True), name='sign-in'),
    path('post-login/', views.postLogin, name='post-login'),
    path('sign-out/', auth_views.LogoutView.as_view(template_name="landbook/sign-out.html"), name='sign-out'), 
]
