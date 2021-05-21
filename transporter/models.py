from django.db import models
from django.db.models.deletion import CASCADE



# Create your models here.
# Create your models here.
class Bus(models.Model):
    
    Bus_name = models.CharField(max_length=30)
    Type = models.CharField(max_length=30)
    No_of_seats=models.IntegerField() 


class Passengers(models.Model):
    
    name = models.CharField(max_length=30)
    age= models.IntegerField()
    Type = models.CharField(max_length=30)
    proof=models.BigIntegerField()
    phone_no=models.BigIntegerField()
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    email= models.CharField(max_length=30)
    password= models.CharField(max_length=30)

class Bus_stops(models.Model):
        
    name1 = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

class Routes(models.Model):
    Busid = models.IntegerField() 
            
    origin=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    cost=models.IntegerField() 
class Tickets(models.Model):
                
    schedulesid=models.IntegerField() 
    passengerid=models.IntegerField() 
class Schedules(models.Model):  
    route=models.CharField(max_length=30)
    field_name = models.CharField(max_length=30)






