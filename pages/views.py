from django.shortcuts import render

# Create your views here.

def pages(req):
 return render(req, 'pages/inicioPages.html')
 