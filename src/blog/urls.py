from django.urls import path
from blog.views import index, posts, users


urlpatterns = [
    path('', posts.index, name='index'),
    path('login/', users.user_login, name='login'),
    path('logout/', users.user_logout, name='logout'),
    path('posts/<int:id>', posts.detail, name='post_detail')
]
