from django.test import TestCase
from .models import Image

class ImageTestClass(TestCase):

  def setUp(self):
    Image.objects.create(image='photo.jpg', caption="beautiful scenary")
  
  def test_image

  
