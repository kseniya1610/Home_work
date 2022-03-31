from django.forms import ModelForm
from .models import Post, User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'categoryType', 'text']


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
