
"""Cinema Ticket Urls """

from django.urls import path,include
from . import views

from .views import food_list , food_detail



app_name="cinematicket"




urlpatterns = [
    # function based views
    path('',food_list,name='food'),
    path('food_detail/<int:pk>/',food_detail,name="food_detail"),

    
  
]   
