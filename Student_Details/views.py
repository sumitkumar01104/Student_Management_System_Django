from django.shortcuts import render, redirect, get_object_or_404
from .models import Form


def index(request):
    return render(request, "index.html")


def Add_Student(request):
    return render(request, "Add_Student.html")


def add_student_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        DoB = request.POST['DoB']
        mobile_no = request.POST['mobile_no']

        Form.objects.create(
            name=name,
            email=email,
            DoB=DoB,
            mobile_no=mobile_no
        )
        return redirect('index')

    return render(request, 'Add_Student.html')


def Show_Student(request):
    students = Form.objects.all()
    return render(request, "Show_Student.html", {'students': students})


def Find_Student(request):
    query = request.GET.get('q')
    if query:
        students = Form.objects.filter(name__icontains=query)
    else:
        students = None

    return render(request, "Find_Student.html", {'students': students})


def Delete_Student(request):
    students = None
    if request.method == 'POST':
        name = request.POST.get('name')
        students = Form.objects.filter(name__icontains=name)

    return render(request, "Delete_Student.html", {'students': students})


def delete_student(request, id):
    student = get_object_or_404(Form, id=id)
    student.delete()
    return redirect('Delete_Student')
