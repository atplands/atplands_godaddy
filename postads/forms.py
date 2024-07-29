from django.db import models  
from django.forms import fields  
from .models import Postad  
from django import forms  
  
  
class PostadImage(forms.ModelForm):  
    class meta:  
        # To specify the model to be used to create form  
        models = Postad  
        # It includes all the fields of model  
        fields = '__all__' 