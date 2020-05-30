from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Image(models.Model):
  img_name = models.CharField(max_length=100, blank=True)
  image = models.ImageField(upload_to='img_posts/')
  caption = models.CharField(max_length=100, blank=True)
  likes = models.ManyToManyField(User, related_name='post_likes')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  def __str__(self):
    return f'{self.user.username} Posted Images'

  def get_absolute_url(self):
    return reverse('image-post-detail', kwargs={'pk': self.pk})

class Comments(models.Model):
  comment = models.CharField(max_length=100)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  img_post = models.ForeignKey(Image, on_delete=models.CASCADE)
  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.comment

   

  



