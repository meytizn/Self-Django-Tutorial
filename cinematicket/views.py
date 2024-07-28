from django.shortcuts import render




def home(request):
  return render(request,'cinematicket/home.html',{})

# Create your views here.
