from django.test import TestCase
from .models import Image

class ImageTestClass(TestCase):

  def setUp(self):
    Image.objects.create(image='UltraUhd ', caption="beautiful scenary")

  
