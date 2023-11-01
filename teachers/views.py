from django.shortcuts import render,redirect
from .models import Student


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
        return redirect ('/viewdata')
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


def edit(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        image = request.FILES['image']
        
        #get the specific student to edit
        student = Student.objects.get(id=id)
        
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
    return render(request, 'edit.html')


# Create your views here.

