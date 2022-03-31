from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post, Author
from django.contrib.auth.models import User
from django.shortcuts import render
from datetime import datetime
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class PostList(ListView):
    model = Post
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 1
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def post(self, request, *args, **kwargs):
        title = request.POST['title']
        text = request.POST['text']
        category = request.POST['categoryType']
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

        new = Post(title=title, text=text, category=category)
        new.save()
        return super().get(request, *args, **kwargs)


class PostDetailView(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = 'flatpages/news_create.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'flatpages/news_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'flatpages/news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


class Search(ListView):
    model = Post
    template_name = 'flatpages/search.html'
    context_object_name = 'search'

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {**super().get_context_data(*args, **kwargs), 'filter': self.get_filter()}


class ProfileView(DetailView):
    model = User
    template_name = 'flatpages/profile.html'
    context_object_name = 'profile'

    def get_object(self, **kwargs):
        id = self.kwargs.user.id
        return User.objects.get(pk=id)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'flatpages/prof_update.html'
    form_class = ProfileForm
    success_url = 'user'
    queryset = User.objects.all()

    def get_object(self, **kwargs):

        return self.request.user


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name='users').exists()
        return context