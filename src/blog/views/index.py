from django.shortcuts import render
from blog.models import Post


def index(request):
    posts = Post.objects.order_by('-published_at')
    return render(request, 'index.html', context={ 'posts': posts })
