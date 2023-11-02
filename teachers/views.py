from django.shortcuts import render,redirect
from .models import Student, Sliders
from django.contrib import messages
from django.core.paginator import Paginator


def home(request):
    return render(request, 'home.html',{'navbar':'Home'})


def about(request):
    return render(request, 'about.html', {'navbar':'about'})


def contact(request):
    return render(request, 'pages/contact.html', {'navbar':'contact'})


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        image = request.FILES['image']
        student = Student(name=name, age=age, image=image, email=email)
        student.save()
        messages.success(request, 'Student added successfully')
        return redirect ('/viewdata')
    return render(request, 'add.html', {'navbar':'add'})

def viewData(request):
    #data = Student.objects.all()
    paginator = Paginator(Student.objects.all(), 2)
    new_page = request.GET.get('page')
    data = paginator.get_page(new_page)
    context = {
        'data':data,
        'navbar':'viewdata',
    }
    return render(request, 'viewdata.html', context)

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    
    return redirect ('/viewdata')


def edit(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        image = request.FILES['image']
        
        #get the specific student to edit
        
        
        #asign the fields with the new data
        student.name = name
        student.age = age
        student.email = email
        student.image = image
        
        if len(request.FILES) != 0:
            if len(student.image) > 0:
                student.image = request.FILES['image']
        
        #save the student with the new data
        student.save()
        return redirect ('/viewdata')
    return render(request, 'edit.html',{'student':student})


def viewStudent(request, id):
    student = Student.objects.get(id=id)
    context = {'student':student}
    return render(request, 'detail.html', context)


def sliders(request):
    sliders = Sliders.objects.all()
    context = {'sliders':sliders,'navbar':'sliders',}
    return render(request, 'slider.html',context)


# Create your views here.

