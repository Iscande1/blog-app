from django.shortcuts import render
from .models import Sneaker

def sneaker_page(request):
    sneakers = Sneaker.objects.all()
    context = {
        "sneakers": sneakers
    }
    return render(request, "./sneaker_page.html", context)
