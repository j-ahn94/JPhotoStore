from django.shortcuts import render



def store_view(request):
    return render(request, 'Store\index.html')


def product_1_view(request):
    return HttpResponse('<h1>This is the product 1</h1>')