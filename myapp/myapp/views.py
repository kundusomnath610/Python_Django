from django.http import HttpResponse


def tese(request):
    print("Test function..")
    return HttpResponse("<h1> Hello this is from python </h1>")