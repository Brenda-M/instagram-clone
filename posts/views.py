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
  DeleteView,
  View
)
from .models import Image, Comment
from django.http import HttpResponse

class HomeView(View):
  def get(self, request, *args, **kwargs):
    user = request.user
    is_following_user_ids = [x.user.id for x in user.is_following.all()]
    qs = Image.objects.filter(user__id__in=is_following_user_ids)
    return render(request, 'posts/index.html', {'images':qs} )

class ImageDetailView(LoginRequiredMixin, DetailView):
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

class CreateCommentView(LoginRequiredMixin, CreateView):
  model = Comment
  fields = ['text']

  def form_valid(self, form):
    img_post = get_object_or_404(Image, pk=self.kwargs.get('pk'))
    form.instance.img_post = img_post
    form.instance.user = self.request.user
    return super().form_valid(form)

  def get_success_url(self, **kwargs):
    pk = self.kwargs.get('pk')
    return reverse('photo_blog-detail', args={pk: 'pk'})

def LikeView(request, pk):
  img_post = get_object_or_404(Image, id=request.POST.get('image_id'))
  img_post.likes.add(request.user)
  return HttpResponseRedirect(reverse('image-post-detail', args=[str(pk)]))

def search(request):
  template = 'posts/search.html'
  query = request.GET.get('q')
  results = User.objects.filter(Q(username__icontains=query))

  return render(request, template, {'users': results})

  
