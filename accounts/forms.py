from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=50,required=True,widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        

class UserForm(forms.ModelForm):

    class Meta:
        model = User 
        fields = ['username', 'first_name','last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

        # def __init__(self, *args, **kwargs):
        #     super(UserForm, self).__init__(*args, **kwargs)
        #     for field in self.fields.values():
        #         field.widget.attrs.update({'class': 'form-control'})


class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ['profile_picture']
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Add Profile Image'})
        }
