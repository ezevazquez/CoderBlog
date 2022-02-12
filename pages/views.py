from django.shortcuts import render

#para importar formulario
from pages.forms import NewPost
from pages.models import Post

# Create your views here.

#Vista del inicio
def pages(req):
 return render(req, 'pages/inicioPages.html')

#vista para crear fomulario
def newPost(req):
    if req.method =='POST':
    
        myForm = NewPost(req.POST)
    
        if myForm.is_valid():
            
            info = myForm.cleaned_data
            
            newPost = Post (img=info['img'], place=info['place'], name=info['name'], title=info['title'], description=info['description'])
            newPost.save()
            
            return render(req,"pages/inicioPages.html")
        
    else:
        myForm = NewPost()
        
    return render(req, "pages/newPost.html",{"myForm":myForm})


 