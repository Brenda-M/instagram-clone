from django.urls import path
from .views import ImageListView, ImageDetailView, ImageCreateView, ImageUpdateView
from . import views

urlpatterns = [
  path('', ImageListView.as_view(), name='index'),
  path('post/<int:pk>/', ImageDetailView.as_view(), name='image-post-detail'),
  path('post/new/', ImageCreateView.as_view(), name='image-create'),
  path('post/<int:pk>/update', ImageUpdateView.as_view(), name='image-update'),

]