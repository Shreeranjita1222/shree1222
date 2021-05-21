from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.urls import path
from transporter import views

urlpatterns= [
   
    path('', views.transporter),
    path("<int:bus_id>", views.transporter)


]

 