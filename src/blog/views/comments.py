from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comment
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

            redirect_to = '/posts/'
            if post.published_at is None:
                redirect_to = '/drafts/'

            # 'post_detail#comments'
            return redirect(redirect_to+str(post.pk)+'#comments', id=post.pk)

    return render(request, 'comments/create.html', { 'post': post, 'form': form })


@login_required
def approve(request, id):
    query_set = Comment.objects.filter(approved=False)
    comment = get_object_or_404(query_set, pk=id)
    comment.approve()

    redirect_to = 'blog:post_detail'
    if comment.post.published_at is None:
        redirect_to = 'blog:draft_detail'

    return redirect(redirect_to, id=comment.post.pk)


@login_required
def delete(request, id):
    comment = get_object_or_404(Comment, pk=id)
    post = comment.post
    comment.delete()

    redirect_to = 'blog:post_detail'
    if post.published_at is None:
        redirect_to = 'blog:draft_detail'

    return redirect(redirect_to, id=post.pk)
