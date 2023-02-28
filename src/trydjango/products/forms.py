from django import forms
from .models import Product
class ProductForm(forms.ModelForm):
    title=forms.CharField(label='title',widget=forms.TextInput(attrs={"placeholder":"your title"}))
    description=forms.CharField(label='description',
                                widget=forms.Textarea(attrs={"rows":20,"cols":20,"placeholder":"Enter description"}))
    price=forms.DecimalField(initial='1.0')
    class Meta:
        model=Product
        fields=[
            'title',
            'description',
            'price'
        ]
    
class RawProductForm(forms.Form):
    title=forms.CharField(label='title',widget=forms.TextInput(attrs={"placeholder":"your title"}))
    description=forms.CharField(label='description',
                                widget=forms.Textarea(attrs={"rows":20,"cols":20,"placeholder":"Enter description"}))
    price=forms.DecimalField(initial='1.0')