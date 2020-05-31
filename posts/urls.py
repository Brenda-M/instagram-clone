from django.urls import path
from .views import (
  # ImageListView, 
  ImageDetailView, 
  ImageCreateView, 
  ImageUpdateView, 
  ImageDeleteView, 
  LikeView,
  CreateCommentView, 
  HomeView

)
from . import views



urlpatterns = [
  path('', HomeView.as_view(), name='index'),
  path('post/<int:pk>/', ImageDetailView.as_view(), name='image-post-detail'),
  path('post/new/', ImageCreateView.as_view(), name='image-create'),
  path('post/<int:pk>/update', ImageUpdateView.as_view(), name='image-update'),
  path('post/<int:pk>/delete', ImageDeleteView.as_view(), name='image-delete'),
  path('like/<int:pk>/',  LikeView, name="like_post"),
  path('find-user/', views.search, name='search_results'),
  path('post/<int:pk>/comment/', CreateCommentView.as_view(), name='image-comment'),
]