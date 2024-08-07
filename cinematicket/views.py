from django.shortcuts import render
from django.views.generic import TemplateView,ListView , DetailView
from .models import Food


# Create your views here.


# Function based views
 
def food_list(request):
    food_list=Food.objects.all()
    context={'food':food_list}
    return render(request,'food_list.html',context)


def food_detail(request,pk):
    food_detail=Food.objects.get(pk=pk)
    return render(request,'food_detail.html',{'food':food_detail})


