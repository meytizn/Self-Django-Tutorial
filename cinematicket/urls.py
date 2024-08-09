
"""Cinema Ticket Urls """

from django.urls import path,include
from . import views

from .views import food_list , food_detail,add_food_cb,update_food,delete_food



app_name="cinematicket"




urlpatterns = [
    # function based views
    path('',food_list,name='food_list'),
    path('food_detail/<int:pk>/',food_detail,name="food_detail"),
    
    path('add_food/',add_food_cb.as_view(),name="add_food"),
    
    path('update_food/<int:pk>/',update_food.as_view(),name="update_food"),
  
    path('delete_food/<int:pk>/',delete_food.as_view(),name="delete_food"),
]   
