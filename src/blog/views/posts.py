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


@login_required
def update(request, id):
    post = get_object_or_404(Post, pk=id)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save()

            redirect_to = 'blog:post_detail'
            if post.published_at is None:
                redirect_to = 'blog:draft_detail'

            return redirect(redirect_to, id=post.pk)

    return render(request, 'posts/update.html', { 'form': form })


@login_required
def delete(request, id):
    post = get_object_or_404(Post, pk=id)

    if request.method == 'POST':
        redirect_to = 'blog:index'
        if post.published_at is None:
            redirect_to = 'blog:drafts'

        post.delete()
        return redirect(redirect_to)

    return render(request, 'posts/delete.html', { 'post': post })
