from django import forms
from . models import post, author

from django.contrib.auth.models import User

# import Registration Form
from django.contrib.auth.forms import UserCreationForm

class createForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['item', 'Date']



class registerUser(UserCreationForm):
    class Meta:
        model = User
        fields = [

            'email',
            'username',
            'password1',
            'password2',
        ]


class createAuthor(forms.ModelForm):
    class Meta:
        model = author
        
        fields = [

            'profile_picture',
            
        ]


