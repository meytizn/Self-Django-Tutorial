from django.shortcuts import render
from django.views.generic import TemplateView,ListView , DetailView
from .models import Food


# Create your views here.


# def home(request):       
#   return render(request,'cinematicket/home.html',{})

class Conssention(ListView):
  model = Food
  template_name = 'concession.html'
  context_object_name='food'
  

class Home(TemplateView):
  template_name='home.html'


class Product(TemplateView):
  template_name='product.html'
