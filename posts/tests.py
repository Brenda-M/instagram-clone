from django.test import TestCase
from django.contrib.auth.models import User
from .models import Image
from .forms import CommentForm

class ImageTestClass(TestCase):

  def setUp(self):
    User.objects.create(username='testUser', email='test@gmail.com')
    Image.objects.create(image='photo.jpg', caption="beautiful scenary",user_id='1')

  def test_get_absolute_url(self):
    image = Image.objects.get(id=1)
    self.assertEquals(image.get_absolute_url(), '/post/1/')
  

class CommentFormTestClass(TestCase):

  def test_comment_field(self):
    form = CommentForm()
    self.assertFalse(form.fields['content'].label==None)
 

  

  
