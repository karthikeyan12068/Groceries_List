from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,"home.html",{})
def contact_view(request,*args,**kwargs):
    return render(request,"contact.html",{})
def about_view(request,*args,**kwargs):
    my_context={
        "mytext":"This about us",
        "mynumber":123,
        "list":['item1','item2','item3','item4']
    }
    return render(request,"about.html",my_context)
