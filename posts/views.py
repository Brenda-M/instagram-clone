from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
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
  ordering = ['-created_at']

class ImageDetailView(DetailView):
  model = Image

class ImageCreateView(LoginRequiredMixin, CreateView):
  model = Image
  fields = ['image', 'caption']
  # success_url=('')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
