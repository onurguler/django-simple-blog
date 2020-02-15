from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post
from blog.forms import CommentForm


def create(request, id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=id)
    else:
        query_set = Post.objects.filter(published_at__isnull=False)
        post = get_object_or_404(query_set, pk=id)

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            redirect_to = 'blog:post_detail'
            if post.published_at is None:
                redirect_to = 'blog:draft_detail'

            return redirect(redirect_to, id=post.pk)

    return render(request, 'comments/create.html', { 'post': post, 'form': form })
