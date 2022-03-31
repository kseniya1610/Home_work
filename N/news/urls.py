from django.urls import path
from .views import PostList, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, ProfileUpdateView, ProfileView

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post'),
    path('create/<int:pk>/', PostCreateView.as_view(), name='news_create'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='news_delete'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='news_edit'),
    path('news/search/',PostList.as_view(), name='search'),
    path('user/<int:pk>/', ProfileView.as_view(), name='user'),
    path('user/<int:pk>/update', ProfileUpdateView.as_view(), name='user_update'),
]
