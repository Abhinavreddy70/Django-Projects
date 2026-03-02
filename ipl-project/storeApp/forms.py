from django import forms
from .models import Product,reviews

# Create your forms here.

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=reviews
        fields='__all__' 