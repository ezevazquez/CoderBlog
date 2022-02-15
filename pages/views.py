from django.shortcuts import render

#para importar formulario
from pages.forms import NewPost
from pages.models import Post

#para poder ver el detalle de las vistas
from django.views.generic.detail import DetailView
#para poder ver el detalle de las vistas
from django.views.generic import ListView
# para editar una vista
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

#Vista del inicio
def pages(req):
    posts = Post.objects.all()#aca traigo todos los posts
    
    context = {"posts":posts}
    
    return render(req, 'pages/inicioPages.html',context)

#vista para crear fomulario
@login_required
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



class PostDetail(DetailView):
    
    model = Post
    template_name = "pages/postDetail.html"

class PostUpdate(UpdateView):
    model: Post
    success_url = '/pages/'
    fields = ['img', 'place', 'name', 'title', 'description']
    
class PostDelete(DeleteView):
    model = Post
    success_url = '/pages/'
    template_name='pages/post_confirm_delete.html'

class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name='pages/postList.html'