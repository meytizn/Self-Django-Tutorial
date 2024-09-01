
"""Cinema Ticket Urls """

from django.urls import path,include
from . import views

from .views import food_list , food_detail,add_food_cb,update_food,delete_food , index,index_detail , category,tag,searchbar



app_name="cinematicket"




urlpatterns = [
    # function based views
    path('food-list/',food_list,name='food_list'),
    path('food_detail/<int:pk>/',food_detail,name="food_detail"),
    
    path('add_food/',add_food_cb.as_view(),name="add_food"),
    
    path('update_food/<int:pk>/',update_food.as_view(),name="update_food"),
  
    path('delete_food/<int:pk>/',delete_food.as_view(),name="delete_food"),

    # template added 
    path('',index,name="index"),
    path('detail/<int:pk>/',index_detail,name='index-detail'),

    # category page
    path('category/<slug:category>/',category,name='category'),
    path('tag/<slug:tag>/',tag,name='tag'),
    
    # searchbar 
    path('search/',searchbar,name='search'),
    
]   
