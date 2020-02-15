from django.urls import path
from blog.views import index, posts, users, drafts, comments


app_name = 'blog'

urlpatterns = [
    path('', posts.index, name='index'),
    path('login/', users.user_login, name='login'),
    path('logout/', users.user_logout, name='logout'),
    path('posts/<int:id>', posts.detail, name='post_detail'),
    path('posts/new', posts.create, name='post_create'),
    path('posts/<int:id>/edit', posts.update, name='post_update'),
    path('posts/<int:id>/remove', posts.delete, name='post_delete'),
    path('posts/<int:id>/publish', posts.publish, name='post_publish'),
    path('posts/<int:id>/comment', comments.create, name='comment_create'),
    path('drafts/', drafts.index, name='drafts'),
    path('drafts/<int:id>', drafts.detail, name='draft_detail')
]
