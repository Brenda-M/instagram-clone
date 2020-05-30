from django.urls import path
from .views import (
  ImageListView, 
  ImageDetailView, 
  ImageCreateView, 
  ImageUpdateView, 
  ImageDeleteView, 
  LikeView
)


urlpatterns = [
  path('', ImageListView.as_view(), name='index'),
  path('post/<int:pk>/', ImageDetailView.as_view(), name='image-post-detail'),
  path('post/new/', ImageCreateView.as_view(), name='image-create'),
  path('post/<int:pk>/update', ImageUpdateView.as_view(), name='image-update'),
  path('post/<int:pk>/delete', ImageDeleteView.as_view(), name='image-delete'),
  path('like/<int:pk>/',  LikeView, name="like_post")
  # path('find-user/', views.search_results, name='search_results')
]