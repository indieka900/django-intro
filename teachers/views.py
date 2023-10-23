from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse("Welcome to Emobilis")


def about(request):
    return HttpResponse("About Emobilis")


def contact(request):
    return HttpResponse("Contact Emobilis")

# Create your views here.
