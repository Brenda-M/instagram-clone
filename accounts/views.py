from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistrationForm
from .models import Profile


def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account created for { username}')
      return redirect('login')

  else: 
    form = RegistrationForm()
  return render(request, 'users/register.html', {'form': form})

class ProfileDetailView(DetailView):
  template_name = 'users/profile.html'

  def get_object(self):
    username = self.kwargs.get("username")
    if username is None:
      raise Http404
    return get_object_or_404(User, username__iexact=username)
  
  def get_context_data(self, *args, **kwargs):
    context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
    user = context['user']
    is_following = False
    if user.profile in self.request.user.is_following.all():
      is_following = True
    context['is_following'] = is_following
    return context

class ProfileFollowToggle(LoginRequiredMixin, View):
  def post(self, request, *args, **kwargs):

    username_to_toggle = request.POST.get("username").strip()
    profile_, is_following = Profile.objects.toggle_follow(request.user, username_to_toggle )


    return redirect(f'/profile/{profile_.user.username}')




