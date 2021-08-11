from django.shortcuts import render
from .models import photo



def store_view(request):
    photos = {'Photos' : photo.objects.all()}
    return render(request, 'Store\index.html', photos)


def cart_view(request):
    return render(request, 'Store\cart.html')