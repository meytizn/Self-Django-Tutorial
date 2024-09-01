from django.shortcuts import render , redirect
from django.views.generic import TemplateView,ListView , DetailView , CreateView,UpdateView,DeleteView
from .models import Food , Category,Tag , Comment
from .forms import CommentForm
from django.urls import reverse,reverse_lazy
from django.core.paginator import Paginator

from django.db.models import Q

# use paginator=4min in video
# from .forms import Foodform



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





# my project begins here ..

def index(request):
    foods=Food.objects.all()
    # using paginator .
    paginator = Paginator(foods,6)  
    page_number = request.GET.get("page")
    food_list = paginator.get_page(page_number)
    return render(request,'index-list.html',{'food_list':food_list})






def index_detail(request,pk):

    
    food=Food.objects.get(pk=pk)
    
    recentfood=Food.objects.all().order_by("-pub_date")[:2]

    category=Category.objects.all().filter(food=food)

    tag=Tag.objects.all().filter(food=food)


    # if request.method == "POST":
    #     form=CommentForm(request.POST)
    #     if form.is_valid():
    #         name=form.cleaned_data['name']
    #         email=form.cleaned_data['email']
    #         message=form.cleaned_data['message']
            
    #         comment=Comment(food=food,name=name,message=message)
    #         comment.save()

    context={'food':food,'recentfood':recentfood,'tag':tag,'category':category,}

    return render(request,'index_detail.html',context)



def category(request,category):
    food=Food.objects.filter(category__slug=category)
    name=category + ' ( Category ) '
    context={'food':food , 'name':name}
    return render(request,'categoryandtag.html',context )


def tag(request,tag):
    food=Food.objects.filter(tag__slug_tag=tag)
    name=tag + '( Tags ) '
    context={'food':food , 'name':name}
    return render(request,'categoryandtag.html',context )






def searchbar(request):
    if request.method=="GET":
        q=request.GET.get("search")
    food_list=Food.objects.filter( Q(name__icontains=q) |Q(description__icontains=q) )


    return render(request,'index-list.html',{'food_list':food_list})

