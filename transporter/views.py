from django.http.response import Http404
from transporter.models import Bus
from django.shortcuts import render
from django.http import HttpResponse
# import Http Response from django

#from django.contrib.auth import REDIRECT_FIELD_NAME, login, authenticate
#from django.contrib.auth.forms import UserCreationForm
#from django.shortcuts import render, redirect
#from busapp.bus.forms import SignUpForm
#from busapp.forms import NewUserForm
#from django.contrib.auth import login
#from django.contrib import messages
#from flask import request        

from .models import Bus
 
# create a function
def transporter(request):
    context= {
        "transporter": Bus.objects.all()

    }
    return render(request, 'transporter.html', context )

def transporter(request, bus_id):
    
    try:
        bus= Bus.objects.get(pk=bus_id)
    except Bus.DoesNotExist:
        raise Http404("Bus does not exist.")
    context= {
        "bus": bus

    }
    return render(request, "bus.html", context)







    




    


    
    
   