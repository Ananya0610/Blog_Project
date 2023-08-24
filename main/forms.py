from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

#built in User model

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    #first_name=forms.CharField(max_length=200, required=True)

    class Meta:
        model=User
        fields=['username','email','password1','password2']
        #all fields defined above

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]