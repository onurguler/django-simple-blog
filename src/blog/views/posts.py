from django.shortcuts import render, get_object_or_404, redirect, reverse, Http404
from django.core.paginator import Paginator
from blog.models import Post
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm


def index(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')

    # Pagination
    page_number = request.GET.get('page') or 1
    per_page = request.GET.get('limit') or 10
    
    paginator = Paginator(posts, per_page)
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', context={ 'posts': page_obj, 
                                                   'page_range': paginator.page_range})


def detail(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=id)
    else:
        query_set = Post.objects.filter(published_at__isnull=False)
        post = get_object_or_404(query_set, pk=id)
    
    return render(request, 'posts/detail.html', context={ 'post': post })


@login_required
def create(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(data=request.POST)

        if form.is_valid():
            post = form.save(commit=False)

            post.author = request.user
            post.save()

            return redirect('blog:post_detail', id=post.pk)

    return render(request, 'posts/create.html', { 'form': form })
