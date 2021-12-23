from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile        
        fields=['first_name','last_name','profile_pic','description','mobile_number','email','category']
        


