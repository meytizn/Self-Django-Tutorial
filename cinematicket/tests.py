from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse



class TestComponent(SimpleTestCase):
  
  def url_tester_if_it_exsist(self):
    response=self.client.get("/product/")
    self.assertEqual(response.status_code,200)

  def url_tester_by_only_name(self):
   response =  self.client.get(reverse('product'))
   self.assertEqual(response.status_code,200)

  def template_tester(self):
    response=self.client.get(reverse('product'))
    self.assertTemplateUsed(response,'product')
  
  def content_template_tester(self):
    response=self.client.get('/product/')
    self.assertContains(response,'<h5>hhh</h5>')


# Create your tests here.
