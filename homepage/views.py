from django.shortcuts import render

# Create your views here.

def homepage(req):
 return render(req, 'homepage/index.html')

def aboutus(req):
 return render(req, 'homepage/aboutus.html')
 