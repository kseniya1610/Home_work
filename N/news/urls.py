from django.urls import path
from .views import PostList, PostDetailView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post'),
    path('create/<int:pk>/', PostCreateView.as_view(), name='news_create'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='news_delete'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='news_edit'),
    path('news/search/',PostList.as_view()),
]
