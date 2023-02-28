from django.shortcuts import render
from .models import Product
from .forms import ProductForm,RawProductForm

def product_create_view(request):
    form=ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context={
        'form':form
    }
    return render(request,'product/create.html',context)

'''
def product_create_view(request):
    if request.method=='POST':
        new_title=request.POST.get('title')
        print(new_title)        
    return render(request,'product/create.html',{})
'''
'''
def product_create_view(request):
    form=RawProductForm()
    if(request.method=='POST'):
        form=RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
    context={
        'form':form
    }    
    return render(request,'product/create.html',context)
'''

def product_detail_view(request):
    obj=Product.objects.get(id=2)
    context={
        'title':obj.title,
        'description':obj.description
    }
    return render(request,'product/detail.html',context)
# Create your views here.
