from django.shortcuts import HttpResponse


def index(request):

    return HttpResponse('<h1>This is the home page</h1>')


