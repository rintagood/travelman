from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from .models import hello


# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=hello.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})
# def hello(request):
#     obj1=hello.objects.all()
#     return render(request,'index.html',{'result1':obj1})


