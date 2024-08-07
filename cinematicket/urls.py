
"""Cinema Ticket Urls """

from django.urls import path,include
from . import views


app_name="cinematicket"




urlpatterns = [
    
    path('home',views.Home.as_view(),name='home'),
    path('product/',views.Product.as_view(),name='product'),
    path('',views.Conssention.as_view(),name='food')
    
  
]   
