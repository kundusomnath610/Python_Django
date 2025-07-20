from django.http import HttpResponse
#import datetime

from django.shortcuts import render


def home(request):
    print("Test function..")
    #date = datetime.datetime.now()
    return render(request, "home.html", {})


def about(request):
    return HttpResponse("<h1> This is about page</h1>")
    #return render(request, "index.html", {})

def services(request):
    return render(request, "services.html", {})

def controller(request):
    return render(request, "controller.html", {})