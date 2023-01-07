from django.shortcuts import render, redirect
from crudoperations_app.models import Student
from crudoperations_app.forms import StudentForm


def get_students_score(request):
    student_list = Student.objects.all()
    return render(request, 'index.html', {'student_list': student_list})


def add_student_score(request):
    student_form = StudentForm()
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
        return redirect('/')
    return render(request, 'add_record.html', {'student_form': student_form})


def delete_student_score(request, idx):
    student = Student.objects.get(id=idx)
    student.delete()
    return redirect('/')


def update_student_record(request, idx):
    student_info = Student.objects.get(id=idx)
    if request.method == 'POST':
        filled_form = StudentForm(request.POST, instance=student_info)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('/')
    return render(request, 'update_record.html', {'student_info': student_info})
