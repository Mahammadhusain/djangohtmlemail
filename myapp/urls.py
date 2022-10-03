from django.urls import path
from .views import *
 
urlpatterns = [
 
    path('', HomeView,name='home'),
    path('send/', send_mail,name='send_mail'),
 
]
