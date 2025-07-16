from django.http import HttpResponse


def tese1(request):
    print("Test function..")
    return HttpResponse("<h1> Hello this is from python </h1>")