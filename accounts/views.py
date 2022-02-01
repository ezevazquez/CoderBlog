from django.shortcuts import render

# Create your views here.

def accounts(req):
 return render(req, 'accounts/inicioAccounts.html')
 