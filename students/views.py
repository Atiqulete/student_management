from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return render(request, 'students/success.html', {'message': 'Student added successfully!'})
        else:
            messages.error(request, 'Error occurred while adding student.')
            return render(request, 'students/error.html', {'message': 'Error occurred while adding student.'})
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def student_edit(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student information updated successfully!')
            return render(request, 'students/success.html', {'message': 'Student information updated successfully!'})
        else:
            messages.error(request, 'Error occurred while updating student.')
            return render(request, 'students/error.html', {'message': 'Error occurred while updating student.'})
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return render(request, 'students/success.html', {'message': 'Student deleted successfully!'})
    return render(request, 'students/student_delete.html', {'student': student})

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'students/student_detail.html', {'student': student})
