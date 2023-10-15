from django.urls import path, include, re_path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('posts', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('posts/create', PostCreateView.as_view(), name='post-create'),
    path('posts/update/<int:pk>', PostUpdateView.as_view(), name='post-update'),
    path('posts/delete/<int:pk>', PostDeleteView.as_view(), name='post-delete'),

]