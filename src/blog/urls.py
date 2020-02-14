from django.urls import path
from blog.views import index, posts


urlpatterns = [
    path('', posts.index, name='index'),
    path('posts/<int:id>', posts.detail, name='post_detail')
]
