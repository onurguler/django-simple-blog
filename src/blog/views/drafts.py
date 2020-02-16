from django.shortcuts import render, get_object_or_404, redirect, reverse, Http404
from django.core.paginator import Paginator
from blog.models import Post
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm


@login_required
def index(request):
    posts = Post.objects.filter(published_at__isnull=True).order_by('-created_at')

    # Pagination
    page_number = request.GET.get('page') or 1
    per_page = request.GET.get('limit') or 10
    
    paginator = Paginator(posts, per_page)
    page_obj = paginator.get_page(page_number)
    return render(request, 'drafts/index.html', context={ 'posts': page_obj, 
                                                   'page_range': paginator.page_range})


@login_required
def detail(request, id):
    query_set = Post.objects.filter(published_at__isnull=True)
    post = get_object_or_404(query_set, pk=id)
    comments = post.comments.all().order_by('-created_at')

    return render(request, 'drafts/detail.html', context={ 'post': post, 'comments': comments })
