
"""Cinema Ticket Urls """

from django.urls import path,include
from . import views

app_name="cinematicket"




urlpatterns = [
    path('',views.home,name='home')
]
