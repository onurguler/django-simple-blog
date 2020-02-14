from django.shortcuts import render, get_object_or_404
from blog.models import Post


def index(request):
    posts = Post.objects.order_by('-published_at')
    return render(request, 'index.html', context={ 'posts': posts })

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/detail.html', context={ 'post': post })
