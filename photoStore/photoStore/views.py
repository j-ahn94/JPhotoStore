from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('This is the home page')


