from django import forms
from .models import Player, stadium

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
       # fields = ['name', 'age', 'role', 'nationality', 'Franchise', 'photo']
        fields = '__all__'


class stadiumForm(forms.ModelForm):
    class Meta:
        model = stadium
        fields = '__all__'