from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from django.views.generic import (
  ListView, 
  DetailView,
  CreateView,
  UpdateView,
  DeleteView,
  View
)
from .forms import CommentForm
from .models import Image, Comment
from django.http import HttpResponse

class HomeView(View):
  def get(self, request, *args, **kwargs):
    user = request.user
    is_following_user_ids = [x.user.id for x in user.is_following.all()]
    qs = Image.objects.filter(user__id__in=is_following_user_ids)
    return render(request, 'posts/index.html', {'images':qs} )

class ImageDetailView( LoginRequiredMixin,FormMixin, DetailView):
  model = Image
  form_class = CommentForm

  def post(self, request, *args, **kwargs):
    if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.img_post = self.get_object()
        post.save()
        text = form.cleaned_data.get('content')
      return HttpResponseRedirect(request.path_info)
    else:
      form=CommentForm()
      return(form)
   
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



# def comment(request):
#   template = 'posts/image_detail.html'
#   # template = 'posts/comment_form.html'
 
#   if request.method == 'POST':
#     form = CommentForm(request.POST)
#     if form.is_valid():
#       form.save()
#       # content = form.cleaned_data.get('content')
#       # new_comment = form.save()
#       # new_comment.save()
#   else:
#     form = CommentForm

  # return render(request, template, {'content':content, 'form':form})

  

  
