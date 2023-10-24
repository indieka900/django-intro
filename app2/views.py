from django.shortcuts import render


def home(request):
    return render(request, 'app2/home.html')


def about(request):
    return render(request, 'app2/about.html')

# Create your views here.
