from django.shortcuts import render
from django.views.generic import ListView
from .models import Image
from django.http import HttpResponse


def index(request):
  context = {
    'images': Image.objects.all()
  }
  return render(request, 'posts/index.html', context)

class ImageListView(ListView):
  model = Image  #tells the listview which model to query inorder to create the listview
  template_name = 'posts/index.html' #naming convention is <app>/<model>_<viewtype>.html
  context_object_name = 'images'
  ordering = ['created_at']