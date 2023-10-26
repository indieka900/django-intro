from django.shortcuts import render


def home(request):
    return render(request, 'app2/home.html')


def about(request):
    context =  {'navbar':'about1'}
    return render(request, 'app2/about.html', context)

# Create your views here.
