from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
  ListView, 
  DetailView,
  CreateView,
  UpdateView,
  DeleteView
)
from .models import Image
from django.http import HttpResponse

def index(request):
  context = {
    'images': Image.objects.all()
  }
  return render(request, 'posts/index.html', context)

class ImageListView(LoginRequiredMixin, ListView):
  model = Image  #tells the listview which model to query inorder to create the listview
  template_name = 'posts/index.html' #naming convention is <app>/<model>_<viewtype>.html
  context_object_name = 'images'
  ordering = ['-id']


class ImageDetailView(DetailView):
  model = Image


class ImageCreateView(LoginRequiredMixin, CreateView):
  model = Image
  fields = ['image', 'caption']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class ImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Image
  fields = ['caption']


  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
  def test_func(self):
    post = self.get_object()
    if self.request.user == post.user:
      return True
    return False


class ImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Image
  success_url = '/'

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.user:
      return True
    return False

def LikeView(request, pk):
  img_post = get_object_or_404(Image, id=request.POST.get('image_id'))
  img_post.likes.add(request.user)
  return HttpResponseRedirect(reverse('image-post-detail', args=[str(pk)]))

def search(request):
  template = 'posts/search.html'
  query = request.GET.get('q')
  results = User.objects.filter(Q(username__icontains=query))

  return render(request, template, {'users': results})

  
