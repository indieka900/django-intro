from django.shortcuts import HttpResponse,render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'pages/contact.html')

# Create your views here.
