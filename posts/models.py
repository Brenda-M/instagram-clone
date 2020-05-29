from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
  image = models.ImageField(upload_to='img_posts/')
  img_name = models.CharField(max_length=100)
  caption = models.CharField(max_length=100)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField()
  



