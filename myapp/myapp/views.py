from django.http import HttpResponse
import datetime


def test(request):
    print("Test function..")
    date = datetime.datetime.now()
    return HttpResponse("<h1> Hello this is from python </h1>" + str(date))


def about(request):
    return HttpResponse("<h1> This is about page</h1>")

def services(request):
    return HttpResponse("<h1> This is services page </h1>")