from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def home(request):
    if request.method=='POST':
       Izoh.objects.create(
            ism=request.POST.get("ism"),
            email=request.POST.get("email"),
            izoh=request.POST.get("izoh"),
        ).save()
    content = {
        "izohlar": Izoh.objects.all()
    }
    return render(request, "index.html", content)


