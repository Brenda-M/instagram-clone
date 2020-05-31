from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.jpg', upload_to='profile_imgs/')
  bio = models.CharField(max_length=100, blank=True)
  followers = models.ManyToManyField(User,related_name='is_following', blank=True)
  created_at = models.DateField(auto_now_add=True)
  update_at = models.DateField(auto_now=True)

  def __str__(self):
    return f'{self.user.username} Profile'

