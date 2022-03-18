from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post
from django.shortcuts import render
from datetime import datetime
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm


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
    template_name = 'templates/flatpages/post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

class PostCreateView(CreateView):
    template_name = 'templates/news_create.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'templates/news_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'templates/news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        return {**super().get_context_data(*args, **kwargs), 'filter':self.get_filter()}

