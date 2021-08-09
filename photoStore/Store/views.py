from django.shortcuts import render
from .models import photo



def store_view(request):
    photos = {'Photos' : photo.objects.all()}
    return render(request, 'Store\index.html', photos)


def product_1_view(request):
    return HttpResponse( '<h1>This is the product 1</h1>')