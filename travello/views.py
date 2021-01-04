from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    dest1 = Destination()
    dest1.name = "Mumbai"
    dest1.price = 700
    dest1.desc= "Amachi Mumbai"
    dest1.img = "destination_1.jpg"
    dest1.offer = True

    dest2 = Destination()
    dest2.name = "Bengaluru"
    dest2.price = "800"
    dest2.desc = "Just code here"
    dest2.img = "destination_2.jpg"
    dest2.offer = False

    dests = [dest1, dest2]
    return render(request,'index.html', {'dests' : dests})
