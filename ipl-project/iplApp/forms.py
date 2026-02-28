from django import forms
from .models import Player, stadium,Profile,User

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
       # fields = ['name', 'age', 'role', 'nationality', 'Franchise', 'photo']
        fields = '__all__'


class stadiumForm(forms.ModelForm):
    class Meta:
        model = stadium
        fields = '__all__'
         # fields = ['name', 'city', 'capacity', 'home_team']


class UserRegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number','address','profile_picture']
        
