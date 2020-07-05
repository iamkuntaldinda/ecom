from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    products = Item.objects.all()
    context = {
        'Products':products
    }
    return render(request,'home.html',context=context)


