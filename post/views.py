from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'post/index.html',context)

def details(request, pk):
    posts = Post.objects.get(id=pk)
    context = {
        'posts':posts,
        }
    return render(request, 'post/details.html',context)