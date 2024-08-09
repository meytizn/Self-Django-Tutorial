from django.shortcuts import render , redirect
from django.views.generic import TemplateView,ListView , DetailView , CreateView,UpdateView,DeleteView
from .models import Food
from django.urls import reverse,reverse_lazy
# from .forms import Foodform

# Create your views here.


# Function based views
 
def food_list(request):
    food_list=Food.objects.all()
    context={'food':food_list}
    return render(request,'food_list.html',context)


def food_detail(request,pk):
    food_detail=Food.objects.get(pk=pk)
    return render(request,'food_detail.html',{'food':food_detail})


# def add_food(request):
#     form=Foodform()

#     if request.method == "POST":
#         form=Foodform(request.POST)
#         if form.is_valid():
#             form.save()
#             redirect('food_list')
#         else:
#             form=Foodform()
#     return render(request,'add_food.html',{'form':form})


class add_food_cb(CreateView):
    model=Food
    template_name='add_food.html'
    fields='__all__'




class update_food (UpdateView):
    model=Food
    context_object_name="food"
    template_name='update_view.html'
    fields='__all__'
    success_url=reverse_lazy("cinematicket:food_list")
    


class delete_food (DeleteView):
    model=Food
    context_object_name="food"
    template_name='delete_food.html'
    fields='__all__'
    success_url=reverse_lazy("cinematicket:food_list")

