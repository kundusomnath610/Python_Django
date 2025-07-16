from django.http import HttpResponse


def test(request):
    print("Test function..")
    return HttpResponse("<h1> Hello this is from python </h1>")