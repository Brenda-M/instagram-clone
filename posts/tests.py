from django.test import TestCase
from django.contrib.auth.models import User
from .models import Image, Comment
from .forms import CommentForm

# class ImageTestClass(TestCase):


#   def test_image_has_user(self):
#     test_user = User.objects.create(username='testUser', email='test@gmail.com')
#     image_test = Image.objects.create(image='photo.jpg', caption="beautiful scenary", user_id=1)
#     image_test.user.set(test_user)
#     self.assertEqual(image_test.user.count(), 1)
  

  # def test_instance(self):
  #   self.assertTrue(isinstance(self.image_test, Image))
  
  # def test_save_image(self):
  #   self.test_user.save()
  #   self.image_test.save_image()
  #   images = Image.objects.all()
  #   self.assertTrue(len(images) > 0)

 

  # def test_get_absolute_url(self):
  #   self.image = Image.objects.get(id=1)
  #   self.assertEquals(self.image.get_absolute_url(), '/post/1/')
  

# class CommentFormTestClass(TestCase):

#   def test_comment_field(self):
#     form = CommentForm()
#     self.assertFalse(form.fields['content'].label==None)


# class CommentTestClass(TestCase):

#   def setUp(self):
#     self.first=Comment(img_post=1, author=, content='Epic performance')

#   def test_instance(self):
#     self.assertTrue(isinstance(self.first,Comment))
 

  

  
