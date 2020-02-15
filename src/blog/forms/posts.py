from django.forms import ModelForm
from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'cover_image', 'text')
