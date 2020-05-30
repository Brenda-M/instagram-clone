from django.urls import path
from .views import ImageListView, ImageDetailView
from . import views

urlpatterns = [
  path('', ImageListView.as_view(), name='index'),
  path('post/<int:pk>/', ImageDetailView.as_view(), name='image-post-detail')

]