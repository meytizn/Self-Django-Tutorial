
"""Cinema Ticket Urls """

from django.urls import path,include
from . import views

from .views import food_list , food_detail,add_food_cb



app_name="cinematicket"




urlpatterns = [
    # function based views
    path('',food_list,name='food_list'),
    path('food_detail/<int:pk>/',food_detail,name="food_detail"),
    
    path('add_food/',add_food_cb.as_view(),name="add_food"),
    
  
]   
