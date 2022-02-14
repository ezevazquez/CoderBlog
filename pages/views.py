from django.shortcuts import render

#para importar formulario
from pages.forms import NewPost
from pages.models import Post

#para poder ver el detalle de las vistas
from django.views.generic.detail import DetailView
# para editar una vista
from django.views.generic.edit import UpdateView
#para eliminar vista
from django.views.generic.edit import DeleteView



# Create your views here.

#Vista del inicio
def pages(req):
    posts = Post.objects.all()#aca traigo todos los posts
    
    context = {"posts":posts}
    
    return render(req, 'pages/inicioPages.html',context)

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

#para ver el detalle de cada post

class PostDetail(DetailView):
    
    model = Post
    template_name = "pages/postDetail.html"
    
    
#para editar un post

class PostUpdate(UpdateView):
    model: Post
    succes_url = "pages/inicioPages.html"
    fields = ['img', 'place', 'name', 'title', 'description']
    


#para eliminar una vista
class PostDelete(DeleteView):
    model = Post
    succes_url = "pages/inicioPages.html"