from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Post
from django.contrib.auth.decorators import login_required


def index(request):
    posts = Post.objects.order_by('-published_at')

    # Pagination
    page_number = request.GET.get('page') or 1
    per_page = request.GET.get('limit') or 10
    
    paginator = Paginator(posts, per_page)
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', context={ 'posts': page_obj, 
                                                   'page_range': paginator.page_range})


def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'posts/detail.html', context={ 'post': post })


@login_required
def create(request):
    return render(request, 'posts/create.html')
