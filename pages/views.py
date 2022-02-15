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
            
            posts = Post.objects.all()#aca traigo todos los posts
    
            context = {"posts":posts}
    
            return render(req, 'pages/inicioPages.html',context)
        
    else:
        myForm = NewPost()
        
    return render(req, "pages/newPost.html",{"myForm":myForm})

#para ver el detalle de cada post

class PostDetail(DetailView):
    
    model = Post
    template_name = "pages/postDetail.html"
    
    




#para eliminar una vista
class PostDelete(DeleteView):
    model = Post
    success_url = '/pages/'
    template_name='pages/post_confirm_delete.html'
    
#para editar un post    
def postUpdate(req, post_id):#para editar el profesor
    post=Post.objects.get(id=post_id)
    
    if req.method == 'POST':
        
        myForm = NewPost(req.POST)#aca llegan todos los datos del html
    
        if myForm.is_valid():
            
            info = myForm.cleaned_data
            
            post.img=info['img']
            post.name=info['name']
            post.place=info['place']
            post.description=info['description']
            post.title=info['title']
                        
            post.save()
            
            return render(req, "pages/inicioPages.html")#volves al inicio
        
    else:
        #creo el formulario con datos que voy a cambiar osea traigo lo que ya tiene cargado el profeso
            myForm=NewPost(initial={'img':post.img, 'place': post.place , 'title': post.title, 'name': post.name, 'description': post.description})
            
    #voy al template para editarlo
    return render(req,"pages/editPost.html",{"myForm":myForm, "post_id":post_id})#hago que retorne de nuevo la lista de profesores
