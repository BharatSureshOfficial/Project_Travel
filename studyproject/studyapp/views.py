from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import  Team

def demo(request):
   obj=place.objects.all()
   teams = Team.objects.all()
   return render(request,"index.html",{'result':obj,'work': teams})


#def addition(request):
#   x=int(request.GET['int1'])
#   y=int(request.GET['int2'])
#   z=x+y
#   return render(request,"result.html",{'result':z})
# Create your views here.
#def about(request):
 #  return render(request,"about.html")
#def maths(request):
#   return HttpResponse('Hello welcome to the world of geometry')