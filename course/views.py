from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Student
from .forms import CourseForm, StudentForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    students = course.students.all()
    return render(request, 'course/course_detail.html', {'course': course, 'students': students})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course/course_form.html', {'form': form})

def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course/course_form.html', {'form': form})

def student_create(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.course = course
            student.save()
            return HttpResponseRedirect(reverse('course_detail', args=[course_id]))
    else:
        form = StudentForm()
    return render(request, 'course/student_form.html', {'form': form})
