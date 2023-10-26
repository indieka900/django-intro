from django.shortcuts import HttpResponse,render


def home(request):
    return render(request, 'home.html',{'navbar':'Home'})


def about(request):
    return render(request, 'about.html', {'navbar':'about'})


def contact(request):
    return render(request, 'pages/contact.html', {'navbar':'contact'})


def add(request):
    return render(request, 'add.html', {'navbar':'add'})

def viewData(request):
    return render(request, 'viewdata.html', {'navbar':'viewdata'})

# Create your views here.

