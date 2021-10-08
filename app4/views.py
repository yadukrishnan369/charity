from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testfun(request):
    return HttpResponse('hello')
def loginfun(request):
    return render(request,'adminlogin.html')
