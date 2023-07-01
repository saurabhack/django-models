from django.shortcuts import render
from django.http import HttpResponse
from .models import products

# Create your views here.
def index(request):
    product1=products()
    product1.name="salar"
    product1.condition="sale"
    product1.price=200


    product2=products()
    product2.name="akshay"
    product2.condition="not sale"
    product2.price=3000

    product3=products()
    product3.name="mitra"
    product3.condition="not sale"
    product3.price=4000

    product1=products()
    product1.name="salar"
    product1.condition="sale"
    product1.price=200
    #productes=[product1,product2,product3]
    #adds=[first,first1,first2]
    return render(request,'index.html',{ 'product1':product1, 'product2':product2, 'product3':product3} )
#{'adds':adds}

def profile(request):
    text2=request.POST['text2']
    text3=request.POST['text3']
    return render(request,'profile.html' ,{'text2':text2 ,'text3':text3})


