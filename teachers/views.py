from django.shortcuts import render,redirect
from .models import Student


def home(request):
    return render(request, 'home.html',{'navbar':'Home'})


def about(request):
    return render(request, 'about.html', {'navbar':'about'})


def contact(request):
    return render(request, 'pages/contact.html', {'navbar':'contact'})


def add(request):
    return render(request, 'add.html', {'navbar':'add'})

def viewData(request):
    data = Student.objects.all()
    context = {
        'data':data,
        'navbar':'viewdata',
    }
    return render(request, 'viewdata.html', context)

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    
    return redirect ('/viewdata')

# Create your views here.

